# `gadgets`

Installed header: `/riscos-resources/Export/Lib/tboxlibs/h/gadgets`

Category: `class`

Purpose: C veneers to the Methods provided by the Window Gadgets

Use it when: Read for generic gadget methods and the built-in gadget families hosted by Toolbox windows.

Related Toolbox manual page: http://www.riscos.com/support/developers/toolbox/windows.html

## Includes

- `kernel.h`
- `toolbox.h`
- `wimp.h`

## Main Types

- `GadgetHeader`
- `ActionButton`
- `ActionButtonSelectedEvent`
- `OptionButton`
- `OptionButtonStateChangedEvent`
- `LabelledBox`
- `Label`
- `RadioButton`
- `RadioButtonStateChangedEvent`
- `DisplayField`
- `WritableField`
- `WritableFieldValueChangedEvent`
- `Slider`
- `SliderValueChangedEvent`
- `Draggable`
- `DraggableDragStartedEvent`
- `DraggableDragEndedEvent`
- `PopUp`
- `PopUpAboutToBeShownEvent`
- `Adjuster`
- `AdjusterClickedEvent`
- `NumberRange`
- `NumberRangeValueChangedEvent`
- `StringSet`
- `StringSetValueChangedEvent`
- `StringSetAboutToBeShownEvent`
- `Button`

## Public Functions

- `gadget_get_bbox`: Returns the bounding box of a gadget
  Prototype: `extern _kernel_oserror *gadget_get_bbox ( unsigned int flags, ObjectId window, ComponentId gadget, BBox *box );`
- `gadget_set_focus`: Sets the focus on a window to a given component
  Prototype: `extern _kernel_oserror *gadget_set_focus ( unsigned int flags, ObjectId window, ComponentId component );`
- `gadget_get_type`: Gets the type for the specified gadget
  Prototype: `extern _kernel_oserror *gadget_get_type ( unsigned int flags, ObjectId window, ComponentId gadget, int *type );`
- `gadget_move_gadget`: Moves an already created gadget in the specified window
  Prototype: `extern _kernel_oserror *gadget_move_gadget ( unsigned int flags, ObjectId window, ComponentId gadget, BBox *new_bbox );`
- `gadget_get_icon_list`: Gets a list of wimp icon numbers (integers) tha are associated with a gadget
  Prototype: `extern _kernel_oserror *gadget_get_icon_list ( unsigned int flags, ObjectId window, ComponentId gadget, int *buffer, int buff_size, int *nbytes );`
- `gadget_get_help_message`: Gets the help message that is associated with a particular gadget
  Prototype: `extern _kernel_oserror *gadget_get_help_message ( unsigned int flags, ObjectId window, ComponentId gadget, char *buffer, int buff_size, int *nbytes );`
- `gadget_set_help_message`: Sets the help message for a particular gadget
  Prototype: `extern _kernel_oserror *gadget_set_help_message ( unsigned int flags, ObjectId window, ComponentId gadget, char *message_text );`
- `gadget_set_flags`: Sets the flags for a particular gadget
  Prototype: `extern _kernel_oserror *gadget_set_flags ( unsigned int flags, ObjectId window, ComponentId gadget, unsigned int new_flags_settings );`
- `gadget_get_flags`: Gets the flags for a particular gadget
  Prototype: `extern _kernel_oserror *gadget_get_flags ( unsigned int flags, ObjectId window, ComponentId gadget, unsigned int *flags_settings );`
- `actionbutton_set_text`: Sets the text that will be displayed in the specified action button
  Prototype: `extern _kernel_oserror *actionbutton_set_text ( unsigned int flags, ObjectId window, ComponentId action_button, char *text );`
- `actionbutton_get_text`: Gets the text that is currently displayed in the specified action button
  Prototype: `extern _kernel_oserror *actionbutton_get_text ( unsigned int flags, ObjectId window, ComponentId action_button, char *buffer, int buff_size, int *nbytes );`
- `actionbutton_set_event`: Sets the toolbox event that will be raised when the button is clicked
  Prototype: `extern _kernel_oserror *actionbutton_set_event ( unsigned int flags, ObjectId window, ComponentId action_button, int event );`
- `actionbutton_get_event`: Gets the toolbox event code that is raised when the button is clicked
  Prototype: `extern _kernel_oserror *actionbutton_get_event ( unsigned int flags, ObjectId window, ComponentId action_button, int *event );`
- `actionbutton_set_click_show`: Sets the Id of the object to show when the button is clicked
  Prototype: `extern _kernel_oserror *actionbutton_set_click_show ( unsigned int flags, ObjectId window, ComponentId action_button, ObjectId object, unsigned int show_flags );`
- `actionbutton_get_click_show`: Gets the Id of the object that will be shown when button is clicked
  Prototype: `extern _kernel_oserror *actionbutton_get_click_show ( unsigned int flags, ObjectId window, ComponentId action_button, ObjectId *object, unsigned int *show_flags );`
- `actionbutton_set_font`: Sets the display font for the specified action button (Requires Wimp >= 380)
  Prototype: `extern _kernel_oserror *actionbutton_set_font ( unsigned int flags, ObjectId window, ComponentId action_button, const char *font_name, int width, int height );`
- `optionbutton_get_label`: Gets the label text for the specified option button
  Prototype: `extern _kernel_oserror *optionbutton_get_label ( unsigned int flags, ObjectId window, ComponentId option_button, char *buffer, int buff_size, int *nbytes );`
- `optionbutton_set_label`: Sets the text of the label for the specified option button
  Prototype: `extern _kernel_oserror *optionbutton_set_label ( unsigned int flags, ObjectId window, ComponentId option_button, char *label );`
- `optionbutton_set_event`: Sets the toolbox event that will be raised when the button is clicked
  Prototype: `extern _kernel_oserror *optionbutton_set_event ( unsigned int flags, ObjectId window, ComponentId option_button, int event );`
- `optionbutton_get_event`: Gets the toolbox event that is raised when the button is clicked
  Prototype: `extern _kernel_oserror *optionbutton_get_event ( unsigned int flags, ObjectId window, ComponentId option_button, int *event );`
- `optionbutton_set_state`: Sets the on/off state of the specified option button
  Prototype: `extern _kernel_oserror *optionbutton_set_state ( unsigned int flags, ObjectId window, ComponentId option_button, int state );`
- `optionbutton_get_state`: Gets the on/off state of the specified option button
  Prototype: `extern _kernel_oserror *optionbutton_get_state ( unsigned int flags, ObjectId window, ComponentId option_button, int *state );`
- `radiobutton_get_label`: Gets the label text for the specified radio button
  Prototype: `extern _kernel_oserror *radiobutton_get_label ( unsigned int flags, ObjectId window, ComponentId radio_button, char *buffer, int buff_size, int *nbytes );`
- `radiobutton_get_state`: Gets the on/off state of the specified radio button
  Prototype: `extern _kernel_oserror *radiobutton_get_state ( unsigned int flags, ObjectId window, ComponentId radio_button, int *state, ComponentId *selected );`
- `radiobutton_set_state`: Sets the on/off state of the specified radio button
  Prototype: `extern _kernel_oserror *radiobutton_set_state ( unsigned int flags, ObjectId window, ComponentId radio_button, int state );`
- `radiobutton_get_event`: Gets the toolbox event that is raised when the button is clicked
  Prototype: `extern _kernel_oserror *radiobutton_get_event ( unsigned int flags, ObjectId window, ComponentId radio_button, int *event );`
- `radiobutton_set_event`: Sets the toolbox event that will be raised when the button is clicked
  Prototype: `extern _kernel_oserror *radiobutton_set_event ( unsigned int flags, ObjectId window, ComponentId radio_button, int event );`
- `radiobutton_set_label`: Sets the text of the label for the specified radio button
  Prototype: `extern _kernel_oserror *radiobutton_set_label ( unsigned int flags, ObjectId window, ComponentId radio_button, char *label );`
- `radiobutton_set_font`: Sets the display font for the specified radio button (Requires Wimp >= 380)
  Prototype: `extern _kernel_oserror *radiobutton_set_font ( unsigned int flags, ObjectId window, ComponentId radio_button, const char *font_name, unsigned int width, unsigned int height );`
- `displayfield_set_font`: Sets the display font for the specified display
  Prototype: `extern _kernel_oserror *displayfield_set_font ( unsigned int flags, ObjectId window, ComponentId display_field, char *font_name, int width, int height );`
- `displayfield_set_value`: Sets the text string to be shown in the specified display field
  Prototype: `extern _kernel_oserror *displayfield_set_value ( unsigned int flags, ObjectId window, ComponentId display_field, char *text );`
- `displayfield_get_value`: Gets the text that is current displayed in the specified display field
  Prototype: `extern _kernel_oserror *displayfield_get_value ( unsigned int flags, ObjectId window, ComponentId display_field, char *buffer, int buff_size, int *nbytes );`
- `writablefield_set_font`: Set the font for the specified writable field
  Prototype: `extern _kernel_oserror *writablefield_set_font ( unsigned int flags, ObjectId window, ComponentId writable_field, char *font_name, int width, int height );`
- `writablefield_set_allowable`: Sets the allowable characters string for the specified writable
  Prototype: `extern _kernel_oserror *writablefield_set_allowable ( unsigned int flags, ObjectId window, ComponentId writable, char *allowed );`
- `writablefield_set_value`: Sets the text string to be shown in the specified writable
  Prototype: `extern _kernel_oserror *writablefield_set_value ( unsigned int flags, ObjectId window, ComponentId writable, char *text );`
- `writablefield_get_value`: Gets the text that is current displayed in the specified writable
  Prototype: `extern _kernel_oserror *writablefield_get_value ( unsigned int flags, ObjectId window, ComponentId writable, char *buffer, int buff_size, int *nbytes );`
- `slider_get_colour`: Gets the desktop colour that is used for the drabbable part of the slider
  Prototype: `extern _kernel_oserror *slider_get_colour ( unsigned int flags, ObjectId window, ComponentId slider, int *bar_colour, int *back_colour );`
- `slider_set_colour`: Sets the desktop colour for the draggable bar in the specified slider
  Prototype: `extern _kernel_oserror *slider_set_colour ( unsigned int flags, ObjectId window, ComponentId slider, int bar_colour, int back_colour );`
- `slider_get_bounds`: Gets the upper/lower and step size for the specified slider
  Prototype: `extern _kernel_oserror *slider_get_bounds( unsigned int flags, ObjectId window, ComponentId slider, int *lower_bound, int *upper_bound, int *step_size );`
- `slider_set_bounds`: Sets the lower/upper bounds and step size for the specified slider
  Prototype: `extern _kernel_oserror *slider_set_bounds( unsigned int flags, ObjectId window, ComponentId slider, int lower_bound, int upper_bound, int step_size );`
- `slider_get_value`: Gets the current value for the specified slider
  Prototype: `extern _kernel_oserror *slider_get_value ( unsigned int flags, ObjectId window, ComponentId slider, int *value );`
- `slider_set_value`: Sets the value of the specified slider
  Prototype: `extern _kernel_oserror *slider_set_value ( unsigned int flags, ObjectId window, ComponentId slider, int value );`
- `draggable_get_state`: Gets the selection state of the specified draggable
  Prototype: `extern _kernel_oserror *draggable_get_state ( unsigned int flags, ObjectId window, ComponentId draggable, int *state );`
- `draggable_set_state`: Sets the selection state of the specified draggable
  Prototype: `extern _kernel_oserror *draggable_set_state ( unsigned int flags, ObjectId window, ComponentId draggable, int state );`
- `draggable_get_sprite`: Gets the sprite that is currently being used for the draggable
  Prototype: `extern _kernel_oserror *draggable_get_sprite ( unsigned int flags, ObjectId window, ComponentId draggable, char *buffer, int buff_size, int *nbytes );`
- `draggable_set_sprite`: Sets the name of the sprite to be used for specified draggable
  Prototype: `extern _kernel_oserror *draggable_set_sprite ( unsigned int flags, ObjectId window, ComponentId draggable, char *sprite_name );`
- `draggable_set_text`: Sets the text to be shown in the specified draggable
  Prototype: `extern _kernel_oserror *draggable_set_text ( unsigned int flags, ObjectId window, ComponentId draggable, char *text );`
- `draggable_get_text`: Gets the text that is shown in the specified draggable
  Prototype: `extern _kernel_oserror *draggable_get_text ( unsigned int flags, ObjectId window, ComponentId draggable, char *buffer, int buff_size, int *nbytes );`
- `popup_get_menu`: Gets the menu object id that will be shown when the popup is clicked
  Prototype: `extern _kernel_oserror *popup_get_menu ( unsigned int flags, ObjectId window, ComponentId popup, ObjectId *menu );`
- `popup_set_menu`: Sets the menu object id that will be shown when the popup is clicked
  Prototype: `extern _kernel_oserror *popup_set_menu ( unsigned int flags, ObjectId window, ComponentId popup, ObjectId menu );`
- `numberrange_get_components`: Gets the component id's for the components which make the number range
  Prototype: `extern _kernel_oserror *numberrange_get_components ( unsigned int flags, ObjectId window, ComponentId number_range, ComponentId *numeric_field, ComponentId *left_adjuster, ComponentId *right_adjuster, ComponentId *slider );`
- `numberrange_set_value`: Sets the value in the NumberRanges display area
  Prototype: `extern _kernel_oserror *numberrange_set_value ( unsigned int flags, ObjectId window, ComponentId number_range, int value );`
- `numberrange_get_value`: Gets the value that is in the NumberRanges display area
  Prototype: `extern _kernel_oserror *numberrange_get_value ( unsigned int flags, ObjectId window, ComponentId number_range, int *value );`
- `numberrange_set_bounds`: Sets the upper/lower bounds, step size and precision for the number range
  Prototype: `extern _kernel_oserror *numberrange_set_bounds ( unsigned int flags, ObjectId window, ComponentId number_range, int lower_bound, int upper_bound, int step_size, int precision );`
- `numberrange_get_bounds`: Gets the lower/upper bounds, step size and precision for the number range
  Prototype: `extern _kernel_oserror *numberrange_get_bounds ( unsigned int flags, ObjectId window, ComponentId number_range, int *lower_bound, int *upper_bound, int *step_size, int *precision );`
- `stringset_get_components`: Gets the components which make up the string set gadget
  Prototype: `extern _kernel_oserror *stringset_get_components ( unsigned int flags, ObjectId window, ComponentId string_set, ComponentId *alphanumeric_field, ComponentId *popup_menu );`
- `stringset_set_selected`: Sets the string that is selected for the specified string set
  Prototype: `extern _kernel_oserror *stringset_set_selected ( unsigned int flags, ObjectId window, ComponentId string_set, char *string_to_select );`
- `stringset_get_selected`: Gets the string that is currently select in the specified string set
  Prototype: `extern _kernel_oserror *stringset_get_selected ( unsigned int flags, ObjectId window, ComponentId string_set, ... );`
- `stringset_set_available`: Sets the list of available strings for the specified string set
  Prototype: `extern _kernel_oserror *stringset_set_available ( unsigned int flags, ObjectId window, ComponentId string_set, char *strings );`
- `stringset_set_allowable`: Sets the allowable characters string for the specified string set
  Prototype: `extern _kernel_oserror *stringset_set_allowable ( unsigned int flags, ObjectId window, ComponentId string_set, char *allowable );`
- `stringset_set_font`: Sets the font for the specified string set
  Prototype: `extern _kernel_oserror *stringset_set_font ( unsigned int flags, ObjectId window, ComponentId string_set, const char *font_name, unsigned int width, unsigned int height );`
- `button_get_flags`: Gets the flags for the specified button
  Prototype: `extern _kernel_oserror *button_get_flags ( unsigned int flags, ObjectId window, ComponentId button, int *icon_flags );`
- `button_set_flags`: Sets the flags for the specified button
  Prototype: `extern _kernel_oserror *button_set_flags ( unsigned int flags, ObjectId window, ComponentId button, int clear_word, int EOR_word );`
- `button_set_value`: Sets the value (text or sprite name) for the specified button
  Prototype: `extern _kernel_oserror *button_set_value ( unsigned int flags, ObjectId window, ComponentId button, char *value );`
- `button_get_value`: Gets the current value for the specified button
  Prototype: `extern _kernel_oserror *button_get_value ( unsigned int flags, ObjectId window, ComponentId button, char *buffer, int buff_size, int *nbytes );`
- `button_get_validation`: Gets the current validation string for the specified button
  Prototype: `extern _kernel_oserror *button_get_validation ( unsigned int flags, ObjectId window, ComponentId button, char *buffer, int buff_size, int *nbytes );`
- `button_set_validation`: Sets the validation string for the specified button
  Prototype: `extern _kernel_oserror *button_set_validation ( unsigned int flags, ObjectId window, ComponentId button, char *value );`
- `button_set_font`: Sets the display font for the specified button
  Prototype: `extern _kernel_oserror *button_set_font ( unsigned int flags, ObjectId window, ComponentId button, char *font_name, int width, int height );`
- `button_get_font`: Reads the display font for the specified button
  Prototype: `extern _kernel_oserror *button_get_font ( unsigned int flags, ObjectId window, ComponentId button, char *font_name, int font_name_max, int *width, int *height, int *nbytes );`

## Public Constants And Method Codes

- `Window_SWIChunkBase` = `0x82880`
- `Gadget_Faded` = `(1u<<31)`
- `Gadget_AtBack` = `(1u<<30)`
- `Gadget_Base` = `64`
- `Gadget_GetFlags` = `(Gadget_Base + 0) /* 64 */`
- `Gadget_SetFlags` = `(Gadget_Base + 1) /* 65 */`
- `Gadget_SetHelpMessage` = `(Gadget_Base + 2) /* 66 */`
- `Gadget_GetHelpMessage` = `(Gadget_Base + 3) /* 67 */`
- `Gadget_GetIconList` = `(Gadget_Base + 4) /* 68 */`
- `Gadget_SetFocus` = `(Gadget_Base + 5) /* 69 */`
- `Gadget_GetType` = `(Gadget_Base + 6) /* 70 */`
- `Gadget_MoveGadget` = `(Gadget_Base + 7) /* 71 */`
- `Gadget_GetBBox` = `(Gadget_Base + 8) /* 72 */`
- `Gadget_Max` = `(Gadget_Base + 63) /* 127 */`
- `ActionButton_IsDefault` = `0x00000001`
- `ActionButton_IsCancel` = `0x00000002`
- `ActionButton_IsLocal` = `0x00000004`
- `ActionButton_ClickShowTransient` = `0x00000008`
- `ActionButton_Base` = `(Gadget_Max + 1) /* 128 */`
- `ActionButton_SetText` = `(ActionButton_Base + 0) /* 128 */`
- `ActionButton_GetText` = `(ActionButton_Base + 1) /* 129 */`
- `ActionButton_SetEvent` = `(ActionButton_Base + 2) /* 130 */`
- `ActionButton_GetEvent` = `(ActionButton_Base + 3) /* 131 */`
- `ActionButton_SetClickShow` = `(ActionButton_Base + 4) /* 132 */`
- `ActionButton_GetClickShow` = `(ActionButton_Base + 5) /* 133 */`
- `ActionButton_SetFont` = `(ActionButton_Base + 6) /* 134 */`
- `ActionButton_Max` = `(ActionButton_Base + 63) /* 191 */`
- `ActionButton_Selected` = `(Window_SWIChunkBase + 1)`
- `ActionButton_Selected_Adjust` = `0x00000001`
- `ActionButton_Selected_Select` = `0x00000004`
- `ActionButton_Selected_Default` = `0x00000008`
- `ActionButton_Selected_Cancel` = `0x00000010`
- `ActionButton_Selected_Local` = `0x00000020`
- `ActionButton_SetClickShow_Transient` = `0x00000001`
- `ActionButton_GetClickShow_Transient` = `0x00000001`
- `OptionButton_Base` = `(ActionButton_Max + 1) /* 192 */`
- `OptionButton_SetLabel` = `(OptionButton_Base + 0) /* 192 */`
- `OptionButton_GetLabel` = `(OptionButton_Base + 1) /* 193 */`
- `OptionButton_SetEvent` = `(OptionButton_Base + 2) /* 194 */`
- `OptionButton_GetEvent` = `(OptionButton_Base + 3) /* 195 */`
- `OptionButton_SetState` = `(OptionButton_Base + 4) /* 196 */`
- `OptionButton_GetState` = `(OptionButton_Base + 5) /* 197 */`
- `OptionButton_Max` = `(OptionButton_Base + 63) /* 255 */`
- `OptionButton_StateChanged` = `(Window_SWIChunkBase + 2)`
- `OptionButton_StateChanged_Adjust` = `0x00000001`
- `OptionButton_StateChanged_Select` = `0x00000004`
- `LabelledBox_Sprite` = `0x00000001`
- `LabelledBox_SpriteIsFilled` = `0x00000002`
- `LabelledBox_Base` = `(OptionButton_Max + 1) /* 256 */`
- `LabelledBox_Max` = `(LabelledBox_Base + 63) /* 319 */`
- `Label_NoBox` = `0x00000001`
- `Label_LeftJustify` = `0x00000000`
- `Label_RightJustify` = `0x00000002`
- `Label_Centred` = `0x00000004`
- `Label_OrientHorizontal` = `0x00000000`
- `Label_OrientUp` = `0x00000010`
- `Label_OrientDown` = `0x00000018`
- `Label_VCentred` = `0x00000000`
- `Label_TopJustify` = `0x00000020`
- `Label_BottomJustify` = `0x00000040`
- `Label_Justification` = `0x00000006 /* Bits 1-2 */`
- `Label_OrientMask` = `0x00000018`
- `Label_VerticalMask` = `0x00000060`
- `Label_Base` = `(LabelledBox_Max + 1) /* 320 */`
- `Label_Max` = `(Label_Base + 63) /* 383 */`
- `RadioButton_GenerateUserStateChanged` = `0x00000001`
- `RadioButton_GenerateSetStateChanged` = `0x00000002`
- `RadioButton_On` = `0x00000004`
- `RadioButton_Base` = `(Label_Max + 1) /* 384 */`
- `RadioButton_SetLabel` = `(RadioButton_Base + 0) /* 384 */`
- `RadioButton_GetLabel` = `(RadioButton_Base + 1) /* 385 */`
- `RadioButton_SetEvent` = `(RadioButton_Base + 2) /* 386 */`
- `RadioButton_GetEvent` = `(RadioButton_Base + 3) /* 387 */`
- `RadioButton_SetState` = `(RadioButton_Base + 4) /* 388 */`
- `RadioButton_GetState` = `(RadioButton_Base + 5) /* 389 */`
- `RadioButton_SetFont` = `(RadioButton_Base + 6) /* 390 */`
- `RadioButton_Max` = `(RadioButton_Base + 63) /* 447 */`
- `RadioButton_StateChanged` = `(Window_SWIChunkBase + 3)`
- `RadioButton_StateChanged_Adjust` = `0x00000001`
- `RadioButton_StateChanged_Select` = `0x00000004`
- `DisplayField_GenerateValueChanged` = `0x00000001`
- `DisplayField_LeftJustify` = `0x00000000`
- `DisplayField_RightJustify` = `0x00000002`
- `DisplayField_Centred` = `0x00000004`
- `DisplayField_Justification` = `0x00000006`
- `DisplayField_Base` = `(RadioButton_Max + 1) /* 448 */`
- `DisplayField_SetValue` = `(DisplayField_Base + 0) /* 448 */`
- `DisplayField_GetValue` = `(DisplayField_Base + 1) /* 449 */`
- `DisplayField_SetFont` = `(DisplayField_Base + 2) /* 450 */`
- `DisplayField_Max` = `(DisplayField_Base + 63) /* 511 */`
- `WritableField_GenerateUserValueChanged` = `0x00000001`
- `WritableField_GenerateSetValueChanged` = `0x00000002`
- `WritableField_LeftJustify` = `0x00000000`
- `WritableField_RightJustify` = `0x00000004`
- `WritableField_Centred` = `0x00000008`
- `WritableField_Justification` = `0x0000000C`
- `WritableField_Password` = `0x00000010`
- `WritableField_Base` = `(DisplayField_Max + 1) /* 512 */`
- `WritableField_SetValue` = `(WritableField_Base + 0) /* 512 */`
- `WritableField_GetValue` = `(WritableField_Base + 1) /* 513 */`
- `WritableField_SetAllowable` = `(WritableField_Base + 2) /* 514 */`
- `WritableField_SetFont` = `(WritableField_Base + 4) /* 516 */`
- `WritableField_Max` = `(WritableField_Base + 63) /* 575 */`
- `WritableField_ValueChanged` = `(Window_SWIChunkBase + 5)`
- `WritableField_ValueChanged_TooLong` = `0x00000001 /* String did not fit into message block */`
- `WritableField_ValueChanged_UserConfirm` = `0x00000002 /* A 'confirm' operation, for example moving out of the box or pressing return */`
- `Slider_GenerateValueChangedEndOfDrag` = `0x00000001`
- `Slider_GenerateValueChangedDuringDrag` = `0x00000002`
- `Slider_GenerateSetValueChanged` = `0x00000004`
- `Slider_Vertical` = `0x00000008`
- `Slider_Draggable` = `0x00000010`
- `Slider_BarColour` = `0x0000F000`
- `Slider_BarColourShift` = `12`
- `Slider_BackgroundColour` = `0x000F0000`
- `Slider_BackgroundColourShift` = `16`
- `Slider_Base` = `(WritableField_Max + 1) /* 576 */`
- `Slider_SetValue` = `(Slider_Base + 0) /* 576 */`
- `Slider_GetValue` = `(Slider_Base + 1) /* 577 */`
- `Slider_SetBounds` = `(Slider_Base + 2) /* 578 */`
- `Slider_GetBounds` = `(Slider_Base + 3) /* 579 */`
- `Slider_SetColour` = `(Slider_Base + 4) /* 580 */`
- `Slider_GetColour` = `(Slider_Base + 5) /* 581 */`
- `Slider_Max` = `(Slider_Base + 63) /* 639 */`
- `Slider_ValueChanged` = `(Window_SWIChunkBase + 6)`
- `Slider_ValueChanged_EndOfDrag` = `1`
- `Slider_ValueChanged_DuringDrag` = `2`
- `Slider_LowerBound` = `0x00000001`
- `Slider_UpperBound` = `0x00000002`
- `Slider_StepSize` = `0x00000004`
- `Draggable_GenerateDragStarted` = `0x00000001`
- `Draggable_Sprite` = `0x00000002`
- `Draggable_Text` = `0x00000004`
- `Draggable_TypeMask` = `0x00000038`
- `Draggable_TypeShift` = `3`
- `Draggable_ToolboxIds` = `0x00000040`
- `Draggable_HasDropShadow` = `0x00000080`
- `Draggable_NotDithered` = `0x00000100`
- `Draggable_Base` = `(Slider_Max + 1) /* 640 */`
- `Draggable_SetSprite` = `(Draggable_Base + 0) /* 640 */`
- `Draggable_GetSprite` = `(Draggable_Base + 1) /* 641 */`
- `Draggable_SetText` = `(Draggable_Base + 2) /* 642 */`
- `Draggable_GetText` = `(Draggable_Base + 3) /* 643 */`
- `Draggable_SetState` = `(Draggable_Base + 4) /* 644 */`
- `Draggable_GetState` = `(Draggable_Base + 5) /* 645 */`
- `Draggable_Max` = `(Draggable_Base + 63) /* 703 */`
- `Draggable_DragStarted` = `(Window_SWIChunkBase + 7)`
- `Draggable_DragEnded` = `(Window_SWIChunkBase + 8)`
- `Draggable_DragStarted_Adjust` = `0x00000001`
- `Draggable_DragStarted_Select` = `0x00000004`
- `Draggable_DragStarted_Shift` = `0x00000008`
- `Draggable_DragStarted_Ctrl` = `0x00000010`
- `Draggable_DragEndedOnToolboxWindow` = `0x00000001`
- `PopUp_GenerateAboutToBeShown` = `0x00000001`
- `PopUp_Base` = `(Draggable_Max + 1) /* 704 */`
- `PopUp_SetMenu` = `(PopUp_Base + 0) /* 704 */`
- `PopUp_GetMenu` = `(PopUp_Base + 1) /* 705 */`
- `PopUp_Max` = `(PopUp_Base + 63) /* 767 */`
- `PopUp_AboutToBeShown` = `(Window_SWIChunkBase + 11)`
- `Adjuster_Increment` = `0x00000001`
- `Adjuster_Decrement` = `0x00000000`
- `Adjuster_UpDown` = `0x00000002`
- `Adjuster_LeftRight` = `0x00000000`
- `AdjusterArrow_Base` = `(PopUp_Max + 1) /* 768 */`
- `AdjusterArrow_Max` = `(AdjusterArrow_Base + 63) /* 831 */`
- `Adjuster_Clicked` = `(Window_SWIChunkBase + 12)`
- `Adjuster_Clicked_Down` = `0x00000000`
- `Adjuster_Clicked_Up` = `0x00000001`
- `NumberRange_GenerateUserValueChanged` = `0x00000001`
- `NumberRange_GenerateSetValueChanged` = `0x00000002`
- `NumberRange_Writable` = `0x00000004`
- `NumberRange_HasNumericalDisplay` = `0x00000008`
- `NumberRange_Adjusters` = `0x00000010`
- `NumberRange_NoSlider` = `0x00000000`
- `NumberRange_SliderType` = `0x00000020`
- `NumberRange_SliderRight` = `(NumberRange_SliderType * 1)`
- `NumberRange_SliderLeft` = `(NumberRange_SliderType * 2)`
- `NumberRange_SliderColour` = `0x00000100 /* multiply by desktop colour number */`
- `NumberRange_SliderTypeMask` = `0x000000E0`
- `NumberRange_Base` = `(AdjusterArrow_Max + 1) /* 832 */`
- `NumberRange_SetValue` = `(NumberRange_Base + 0) /* 832 */`
- `NumberRange_GetValue` = `(NumberRange_Base + 1) /* 833 */`
- `NumberRange_SetBounds` = `(NumberRange_Base + 2) /* 834 */`
- `NumberRange_GetBounds` = `(NumberRange_Base + 3) /* 835 */`
- `NumberRange_GetComponents` = `(NumberRange_Base + 4) /* 836 */`
- `NumberRange_Max` = `(NumberRange_Base + 63) /* 895 */`
- `NumberRange_GetComponents_ReturnNumericalField` = `0x00000001`
- `NumberRange_GetComponents_ReturnLeftAdjuster` = `0x00000002`
- `NumberRange_GetComponents_ReturnRightAdjuster` = `0x00000004`
- `NumberRange_GetComponents_ReturnSlider` = `0x00000008`
- `NumberRange_LowerBound` = `0x00000001`
- `NumberRange_UpperBound` = `0x00000002`
- `NumberRange_StepSize` = `0x00000004`
- `NumberRange_Precision` = `0x00000008`
- `NumberRange_ValueChanged` = `(Window_SWIChunkBase + 13)`
- `StringSet_GenerateUserValueChanged` = `0x00000001`
- `StringSet_GenerateSetValueChanged` = `0x00000002`
- `StringSet_Writable` = `0x00000004`
- `StringSet_GenerateAboutToBeShown` = `0x00000008`
- `StringSet_NoDisplay` = `0x00000010`
- `StringSet_GetComponents_ReturnAlphaNumericField` = `0x00000001`
- `StringSet_GetComponents_ReturnPopUpMenu` = `0x00000002`
- `StringSet_Base` = `(NumberRange_Max + 1) /* 896 */`
- `StringSet_SetAvailable` = `(StringSet_Base + 0) /* 896 */`
- `StringSet_SetSelected` = `(StringSet_Base + 2) /* 898 */`
- `StringSet_GetSelected` = `(StringSet_Base + 3) /* 899 */`
- `StringSet_SetAllowable` = `(StringSet_Base + 4) /* 900 */`
- `StringSet_GetAllowable` = `(StringSet_Base + 5) /* 901 */`
- `StringSet_GetComponents` = `(StringSet_Base + 6) /* 902 */`
- `StringSet_SetFont` = `(StringSet_Base + 7) /* 903 */`
- `StringSet_Max` = `(StringSet_Base + 63) /* 959 */`
- `StringSet_IndexedSelection` = `0x00000001`
- `StringSet_ValueChanged` = `(Window_SWIChunkBase + 14)`
- `StringSet_AboutToBeShown` = `(Window_SWIChunkBase + 15)`
- `StringSet_ValueChanged_TooLong` = `0x00000001`
- `Button_TaskSpriteArea` = `0x00000001`
- `Button_AllowMenuClicks` = `0x00000002`
- `Button_Base` = `(StringSet_Max + 1) /* 960 */`
- `Button_GetFlags` = `(Button_Base + 0) /* 960 */`
- `Button_SetFlags` = `(Button_Base + 1) /* 961 */`
- `Button_SetValue` = `(Button_Base + 2) /* 962 */`
- `Button_GetValue` = `(Button_Base + 3) /* 963 */`
- `Button_SetValidation` = `(Button_Base + 4) /* 964 */`
- `Button_GetValidation` = `(Button_Base + 5) /* 965 */`
- `Button_SetFont` = `(Button_Base + 6) /* 966 */`
- `Button_GetFont` = `(Button_Base + 7) /* 967 */`
- `Button_Max` = `(Button_Base + 63) /* 1023 */`
- `ActionButton_Type` = `(sizeof(ActionButton) + sizeof(GadgetHeader)) << 16 | ActionButton_Base`
- `OptionButton_Type` = `(sizeof(OptionButton) + sizeof(GadgetHeader)) << 16 | OptionButton_Base`
- `LabelledBox_Type` = `(sizeof(LabelledBox) + sizeof(GadgetHeader)) << 16 | LabelledBox_Base`
- `RadioButton_Type` = `(sizeof(RadioButton) + sizeof(GadgetHeader)) << 16 | RadioButton_Base`
- `DisplayField_Type` = `(sizeof(DisplayField) + sizeof(GadgetHeader)) << 16 | DisplayField_Base`
- `WritableField_Type` = `(sizeof(WritableField) + sizeof(GadgetHeader)) << 16 | WritableField_Base`
- `Slider_Type` = `(sizeof(Slider) + sizeof(GadgetHeader)) << 16 | Slider_Base`
- `Draggable_Type` = `(sizeof(Draggable) + sizeof(GadgetHeader)) << 16 | Draggable_Base`
- `PopUp_Type` = `(sizeof(PopUp) + sizeof(GadgetHeader)) << 16 | PopUp_Base`
- `AdjusterArrow_Type` = `(sizeof(Adjuster) + sizeof(GadgetHeader)) << 16 | AdjusterArrow_Base`
- `NumberRange_Type` = `(sizeof(NumberRange) + sizeof(GadgetHeader)) << 16 | NumberRange_Base`
- `StringSet_Type` = `(sizeof(StringSet) + sizeof(GadgetHeader)) << 16 | StringSet_Base`
- `Button_Type` = `(sizeof(Button) + sizeof(GadgetHeader)) << 16 | Button_Base`
