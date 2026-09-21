from __future__ import annotations

from typing import Any

from libqtile.backend.base import Window
from libqtile.command.base import expose_command
from libqtile.config import ScreenRect
from libqtile.layout.base import _SimpleLayoutBase


class CenterMaster(_SimpleLayoutBase):
    """Centered master with balanced left and right stacks.

    Client zero remains master. With two clients the master uses the left side.
    With three or more clients it moves to the centre and secondary clients are
    distributed alternately between both side stacks. Promotion to master is an
    explicit operation so horizontal movement never replaces master by accident.
    """

    defaults = [
        ("border_focus", "#bd93f9", "Focused border colour."),
        ("border_normal", "#44475a", "Unfocused border colour."),
        ("border_width", 2, "Border width."),
        ("margin", 8, "Window margin."),
        ("ratio", 0.40, "Master width with three or more clients."),
        ("two_ratio", 0.68, "Master width with two clients."),
        ("min_ratio", 0.30, "Minimum centered master ratio."),
        ("max_ratio", 0.60, "Maximum centered master ratio."),
        ("ratio_increment", 0.03, "Master resize step."),
        ("new_client_position", "bottom", "Where new secondary clients are inserted."),
    ]

    def __init__(self, **config: Any) -> None:
        super().__init__(**config)
        self.add_defaults(CenterMaster.defaults)
        self._default_ratio = self.ratio
        self._default_two_ratio = self.two_ratio

    def add_client(self, client: Window) -> None:
        """Keep the first client as master and add new clients as secondary."""
        if not self.clients:
            self.clients.append(client)
        elif self.new_client_position == "top":
            self.clients.insert(1, client)
        else:
            self.clients.append(client)
        self.clients.current_client = client

    def _roles(self) -> tuple[Window | None, list[Window], list[Window]]:
        if not self.clients:
            return None, [], []
        master = self.clients[0]
        secondary = list(self.clients)[1:]
        return master, secondary[0::2], secondary[1::2]

    @staticmethod
    def _split_height(screen: ScreenRect, count: int, index: int) -> tuple[int, int]:
        base = screen.height // count
        remainder = screen.height % count
        y = screen.y + index * base + min(index, remainder)
        height = base + (1 if index < remainder else 0)
        return y, height

    def _geometry(self, client: Window, screen: ScreenRect) -> tuple[int, int, int, int]:
        master, left, right = self._roles()
        count = len(self.clients)

        if count == 1:
            return screen.x, screen.y, screen.width, screen.height

        if count == 2:
            master_width = int(screen.width * self.two_ratio)
            if client is master:
                return screen.x, screen.y, master_width, screen.height
            return screen.x + master_width, screen.y, screen.width - master_width, screen.height

        master_width = int(screen.width * self.ratio)
        side_width = (screen.width - master_width) // 2
        right_width = screen.width - master_width - side_width
        master_x = screen.x + side_width

        if client is master:
            return master_x, screen.y, master_width, screen.height
        if client in left:
            index = left.index(client)
            y, height = self._split_height(screen, len(left), index)
            return screen.x, y, side_width, height

        index = right.index(client)
        y, height = self._split_height(screen, len(right), index)
        return master_x + master_width, y, right_width, height

    def configure(self, client: Window, screen_rect: ScreenRect) -> None:
        if client not in self.clients:
            client.hide()
            return
        x, y, width, height = self._geometry(client, screen_rect)
        border = 0 if len(self.clients) == 1 else self.border_width
        colour = self.border_focus if client.has_focus else self.border_normal
        client.place(
            x, y,
            max(1, width - border * 2),
            max(1, height - border * 2),
            border, colour, margin=self.margin,
        )
        client.unhide()

    def _focus(self, target: Window | None) -> None:
        if target is None:
            return
        self.clients.current_client = target
        self.group.focus(target, True)

    def _column(self, client: Window) -> tuple[str, list[Window]]:
        master, left, right = self._roles()
        if client is master:
            return "master", [client]
        if client in left:
            return "left", left
        return "right", right

    @staticmethod
    def _closest_vertical(source: Window, candidates: list[Window]) -> Window | None:
        if not candidates:
            return None
        sy = source.y + source.height / 2
        return min(candidates, key=lambda win: abs((win.y + win.height / 2) - sy))

    @expose_command()
    def left(self) -> None:
        current = self.clients.current_client
        if current is None:
            return
        column, _ = self._column(current)
        master, left, _ = self._roles()
        if column == "right":
            self._focus(master)
        elif column == "master":
            self._focus(self._closest_vertical(current, left))

    @expose_command()
    def right(self) -> None:
        current = self.clients.current_client
        if current is None:
            return
        column, _ = self._column(current)
        master, _, right = self._roles()
        if column == "left":
            self._focus(master)
        elif column == "master":
            self._focus(self._closest_vertical(current, right))

    @expose_command()
    def up(self) -> None:
        current = self.clients.current_client
        if current is None:
            return
        _, stack = self._column(current)
        if len(stack) > 1:
            self._focus(stack[(stack.index(current) - 1) % len(stack)])

    @expose_command()
    def down(self) -> None:
        current = self.clients.current_client
        if current is None:
            return
        _, stack = self._column(current)
        if len(stack) > 1:
            self._focus(stack[(stack.index(current) + 1) % len(stack)])

    def _swap_clients(self, first: Window, second: Window) -> None:
        first_index = self.clients.index(first)
        second_index = self.clients.index(second)
        self.clients[first_index], self.clients[second_index] = (
            self.clients[second_index], self.clients[first_index]
        )
        self.clients.current_client = first
        self.group.layout_all()
        self.group.focus(first, True)

    @expose_command()
    def swap_main(self) -> None:
        """Promote the focused secondary window to master."""
        current = self.clients.current_client
        if current is None or not self.clients or current is self.clients[0]:
            return
        self._swap_clients(current, self.clients[0])

    def _move_between_stacks(self, destination: str) -> None:
        current = self.clients.current_client
        if current is None or current is self.clients[0] or len(self.clients) < 3:
            return
        _, left, right = self._roles()
        source = left if current in left else right
        target = right if destination == "right" else left
        if source is target:
            return
        if target:
            other = self._closest_vertical(current, target)
            if other is not None:
                self._swap_clients(current, other)
                return
        index = self.clients.index(current)
        if destination == "left" and index % 2 == 0:
            self.clients[index - 1], self.clients[index] = self.clients[index], self.clients[index - 1]
        elif destination == "right" and index % 2 == 1 and index + 1 < len(self.clients):
            self.clients[index], self.clients[index + 1] = self.clients[index + 1], self.clients[index]
        self.clients.current_client = current
        self.group.layout_all()

    @expose_command()
    def shuffle_left(self) -> None:
        self._move_between_stacks("left")

    @expose_command()
    def shuffle_right(self) -> None:
        self._move_between_stacks("right")

    def _shuffle_vertical(self, direction: int) -> None:
        current = self.clients.current_client
        if current is None or current is self.clients[0]:
            return
        _, stack = self._column(current)
        if len(stack) < 2:
            return
        target = stack[(stack.index(current) + direction) % len(stack)]
        self._swap_clients(current, target)

    @expose_command()
    def shuffle_up(self) -> None:
        self._shuffle_vertical(-1)

    @expose_command()
    def shuffle_down(self) -> None:
        self._shuffle_vertical(1)

    def _change_ratio(self, amount: float) -> None:
        if len(self.clients) == 2:
            self.two_ratio = min(0.80, max(0.55, self.two_ratio + amount))
        else:
            self.ratio = min(self.max_ratio, max(self.min_ratio, self.ratio + amount))
        self.group.layout_all()

    @expose_command()
    def grow_left(self) -> None:
        self._change_ratio(self.ratio_increment)

    @expose_command()
    def grow_right(self) -> None:
        self._change_ratio(-self.ratio_increment)

    @expose_command()
    def grow_up(self) -> None:
        return

    @expose_command()
    def grow_down(self) -> None:
        return

    @expose_command()
    def normalize(self) -> None:
        self.ratio = self._default_ratio
        self.two_ratio = self._default_two_ratio
        self.group.layout_all()

    @expose_command()
    def info(self) -> dict[str, Any]:
        info = super().info()
        master, left, right = self._roles()
        info.update({
            "master": master.name if master else None,
            "left": [client.name for client in left],
            "right": [client.name for client in right],
            "ratio": self.ratio,
            "two_ratio": self.two_ratio,
        })
        return info
