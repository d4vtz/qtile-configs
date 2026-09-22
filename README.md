# qtile-configs

Base de un entorno de escritorio Wayland propio: **Qtile** como compositor y gestor de ventanas, y **Quickshell** como shell gráfica.

La implementación actual cubre el núcleo de Qtile. La barra de Qtile es provisional y será reemplazada por la barra de Quickshell.

## Arquitectura

```text
config.py
desktop/
├── appearance/
│   └── theme.py
└── qtile/
    ├── core/
    │   ├── apps.py
    │   ├── groups.py
    │   ├── hooks.py
    │   ├── input.py
    │   ├── keys.py
    │   ├── mouse.py
    │   ├── screens.py
    │   └── settings.py
    └── layouts/
        └── standard.py
```

`config.py` es sólo el adaptador que expone a Qtile las variables que espera.

## Dependencias

Base:

- qtile-git
- kitty
- rofi
- pipewire / wireplumber
- brightnessctl
- mypy (recomendado para qtile check)

## Funciones actuales

- 7 workspaces.
- Scratchpad de terminal con `Super + grave`.
- Navegación, movimiento y redimensionado con flechas.
- MonadTall, Columns y Max.
- Ventanas flotantes y fullscreen.
- Reglas flotantes para diálogos y utilidades.
- Touchpad Wayland con tap, drag, disable-while-typing y scroll de dos dedos.
- Teclado latinoamericano.
- Controles multimedia para PipeWire/WirePlumber.
- Control de brillo.
- Reconfiguración automática de pantallas.
- Barra Qtile temporal con workspaces, layout, título, CPU, RAM, audio, batería y reloj.
- Tema Dracula compartido como base visual.

## Atajos

| Atajo | Acción |
|---|---|
| Super + Return | Terminal |
| Super + Space | Launcher |
| Super + E | Archivos |
| Super + 1..7 | Cambiar workspace |
| Super + Shift + 1..7 | Mover ventana al workspace |
| Super + flechas | Cambiar foco |
| Super + Shift + flechas | Mover ventana |
| Super + Ctrl + flechas | Redimensionar |
| Super + V | Floating |
| Super + F | Fullscreen |
| Super + Tab | Siguiente layout |
| Super + grave | Scratchpad |
| Super + Q | Cerrar ventana |
| Super + Ctrl + R | Recargar Qtile |
| Super + Ctrl + Shift + Q | Salir de Qtile |

## Validación

```bash
qtile check
```

Tras actualizar el repositorio, valida antes de recargar una sesión activa.

## Próximas capas

1. Shell Quickshell: barra, launcher, dashboard, notificaciones, clipboard, OSD y sesión.
2. IPC entre Qtile, servicios y Quickshell.
3. Integración visual y efectos del compositor.


## Sesión systemd --user

Los servicios persistentes viven en `systemd/user/` y se agrupan bajo
`qtile-session.target`. Qtile importa el entorno Wayland/D-Bus al arrancar y
activa el target una sola vez.

Instalación inicial:

```bash
./scripts/install-user-services.sh
```

Después de instalar los enlaces, cierra la sesión gráfica y vuelve a entrar.
Actualmente el target administra el agente PolicyKit de KDE, KDE Connect y
Quickshell. Los servicios pueden deshabilitarse individualmente con
`systemctl --user disable --now <unidad>`.


## dqtile package

The Qtile entry point is intentionally minimal: `config.py` imports the public API from `dqtile`.

The package separates responsibilities into `core`, `layouts`, `theme`, `ui`, and `services`. During the migration, compatibility modules delegate to the existing `desktop.qtile` implementation so behaviour remains unchanged while modules can be moved incrementally without a flag day rewrite.

```text
dqtile/
├── config.py
├── core/
├── layouts/
├── services/
├── theme/
└── ui/
```

This keeps the existing desktop/session architecture and custom layouts while providing a stable package boundary for future widgets, services, themes and multi-monitor support.
