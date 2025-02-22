# Curtainview

The curtainview widget can accommodate multiple curtain widgets. On the created curtain widgets, you can place application-related information such as application menus or other pertinent content. This widget can be extended as needed and customized according to requirements.
As illustrated in figure, the curtainview is composed of five curtains, arranged in the following five directions: top, bottom, right, left, and center.
<br>
<div style="text-align: center"><img width="400" img src="https://foruda.gitee.com/images/1727088694333469506/7c243250_13408154.png" /></div>
<br>

## Usage

### Create Curtainview Widget

The function [gui_curtainview_create(void *parent, const char *name, int16_t x, int16_t y, int16_t w, int16_t h)](#gui_curtainview_create) is utilized to create a container that is capable of housing the curtain widget.

### Callback

Once the curtain extension is finished, you can configure certain callback events through the use of  [gui_curtainview_set_done_cb(gui_curtainview_t *_this, void (*cb)(gui_curtainview_t *_this))](#gui_curtainview_set_done_cb).

## Example

Please refer to the section: [Curtain](./gui_curtain.md)


## API


```eval_rst

.. doxygenfile:: gui_curtainview.h

```
