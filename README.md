# qtile-configs

Configuración modular mínima para Qtile 0.37.x sobre Wayland.

## Estructura

- `config.py`: punto de entrada.
- `keys.py`: atajos de teclado.
- `groups.py`: siete grupos/workspaces.
- `layouts.py`: layouts y reglas de ventanas flotantes.
- `screens.py`: barra y pantallas.
- `mouse.py`: controles del ratón para ventanas flotantes.
- `settings.py`: comportamiento global de Qtile.
- `theme.py`: paleta Dracula y tamaños básicos.

## Dependencias iniciales

La configuración asume:

- `qtile-git`
- `kitty`
- `rofi`

Los widgets de CPU, memoria, volumen, batería y systray son los nativos de Qtile.

## Instalación

```bash
git clone https://github.com/d4vtz/qtile-configs.git ~/.config/qtile
qtile check
```

Si `~/.config/qtile` ya existe, respáldalo antes.

## Atajos principales

| Atajo | Acción |
|---|---|
| `Super + Return` | Terminal |
| `Super + Space` | Launcher |
| `Super + 1..7` | Cambiar de grupo |
| `Super + Shift + 1..7` | Mover ventana al grupo |
| `Super + flechas` | Cambiar foco |
| `Super + Shift + flechas` | Mover ventana |
| `Super + Ctrl + flechas` | Redimensionar |
| `Super + V` | Floating |
| `Super + F` | Fullscreen |
| `Super + Tab` | Siguiente layout |
| `Super + Shift + Q` | Cerrar ventana |
| `Super + Ctrl + R` | Recargar configuración |

## Layouts iniciales

1. `MonadTall`
2. `Columns`
3. `Max`

La siguiente etapa será implementar `CenterMaster` como layout nativo de Qtile y después integrar Quickshell.
