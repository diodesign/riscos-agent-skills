# Toolbox OSLib components

Toolbox core plus object and gadget modules such as Window, Menu, SaveAs, Iconbar, and writable fields.

Public C headers are under `.../OSLib/Toolbox/h`. The matching `hdr/` directory contains the parallel assembler/DefMod interface names for the same logical components.

## `ToolAction.h`

Types: `toolaction_object`, `toolaction_action_selected`, `toolaction_set_ident_flags`

Functions: `xtoolaction_set_ident`, `toolaction_set_ident`, `xtoolaction_get_ident`, `toolaction_get_ident`, `xtoolaction_set_action`, `toolaction_set_action`, `xtoolaction_get_action`, `toolaction_get_action`, `xtoolaction_set_click_show`, `toolaction_set_click_show`, `xtoolaction_get_click_show`, `toolaction_get_click_show`, `xtoolaction_set_state`, `toolaction_set_state`, `xtoolaction_get_state`, `toolaction_get_state`, `xtoolaction_set_pressed`, `toolaction_set_pressed`, `xtoolaction_get_pressed`, `toolaction_get_pressed`

## `actionbutton.h`

Types: `actionbutton_object`

Functions: `xactionbutton_set_text`, `actionbutton_set_text`, `xactionbutton_get_text`, `actionbutton_get_text`, `xactionbutton_set_action`, `actionbutton_set_action`, `xactionbutton_get_action`, `actionbutton_get_action`, `xactionbutton_set_click_show`, `actionbutton_set_click_show`, `xactionbutton_get_click_show`, `actionbutton_get_click_show`

## `adjuster.h`

Types: `adjuster_object`, `adjuster_action_clicked`

Functions: none

## `button.h`

Types: `button_object`

Functions: `xbutton_get_flags`, `button_get_flags`, `xbutton_set_flags`, `button_set_flags`, `xbutton_set_value`, `button_set_value`, `xbutton_get_value`, `button_get_value`, `xbutton_set_validation`, `button_set_validation`, `xbutton_get_validation`, `button_get_validation`, `xbutton_set_font`, `button_set_font`

## `colourdbox.h`

Types: `colourdbox_object`, `colourdbox_action_about_to_be_shown`, `colourdbox_colour_model`, `colourdbox_colour_model_base`, `colourdbox_action_dialogue_completed`, `colourdbox_action_colour_selected`, `colourdbox_flags`, `colourdbox_colour_flags`, `colourdbox_full`, `colourdbox_dialogue_completed_flags`

Functions: `xcolourdbox_get_wimp_handle`, `colourdbox_get_wimp_handle`, `xcolourdbox_get_dialogue_handle`, `colourdbox_get_dialogue_handle`, `xcolourdbox_set_colour`, `colourdbox_set_colour`, `xcolourdbox_get_colour`, `colourdbox_get_colour`, `xcolourdbox_set_colour_model`, `colourdbox_set_colour_model`, `xcolourdbox_get_colour_model`, `colourdbox_get_colour_model`, `xcolourdbox_set_none_available`, `colourdbox_set_none_available`, `xcolourdbox_get_none_available`, `colourdbox_get_none_available`

## `colourmenu.h`

Types: `colourmenu_object`, `colourmenu_action_about_to_be_shown`, `colourmenu_action_selection`, `colourmenu_flags`, `colourmenu_colour`, `colourmenu_full`

Functions: `xcolourmenu_set_colour`, `colourmenu_set_colour`, `xcolourmenu_get_colour`, `colourmenu_get_colour`, `xcolourmenu_set_none_available`, `colourmenu_set_none_available`, `xcolourmenu_get_none_available`, `colourmenu_get_none_available`, `xcolourmenu_set_title`, `colourmenu_set_title`, `xcolourmenu_get_title`, `colourmenu_get_title`

## `dcs.h`

Types: `dcs_object`, `dcs_action_about_to_be_shown`, `dcs_flags`, `dcs_full`

Functions: `xdcs_get_window_id`, `dcs_get_window_id`, `xdcs_set_message`, `dcs_set_message`, `xdcs_get_message`, `dcs_get_message`, `xdcs_set_title`, `dcs_set_title`, `xdcs_get_title`, `dcs_get_title`

## `ddeutils.h`

Types: `ddeutils_message_processing_file`, `ddeutils_message_errors_in`, `ddeutils_message_error_details`, `ddeutils_message_info_for_file`, `ddeutils_message_info_details`

Functions: `xddeutils_prefix`, `xddeutils_set_cl_size`, `xddeutils_set_cl`, `xddeutils_get_cl_size`, `xddeutils_get_cl`, `xddeutils_throwback_register`, `xddeutils_throwback_un_register`, `xddeutils_throwback_start`, `xddeutils_throwback_send`, `ddeutils_throwback_send`, `xddeutils_throwback_end`

## `displayfield.h`

Types: `displayfield_object`

Functions: `xdisplayfield_set_value`, `displayfield_set_value`, `xdisplayfield_get_value`, `displayfield_get_value`, `xdisplayfield_set_font`, `displayfield_set_font`

## `draganobject.h`

Types: `draganobject_function`

Functions: `xdraganobject_start`, `draganobject_start`, `xdraganobject_stop`

## `draggable.h`

Types: `draggable_object`, `draggable_action_drag_ended`

Functions: `xdraggable_set_sprite`, `draggable_set_sprite`, `xdraggable_get_sprite`, `draggable_get_sprite`, `xdraggable_set_text`, `draggable_set_text`, `xdraggable_get_text`, `draggable_get_text`, `xdraggable_set_state`, `draggable_set_state`, `xdraggable_get_state`, `draggable_get_state`

## `fileinfo.h`

Types: `fileinfo_object`, `fileinfo_action_about_to_be_shown`, `fileinfo_flags`, `fileinfo_full`

Functions: `xfileinfo_get_window_id`, `fileinfo_get_window_id`, `xfileinfo_set_modified`, `fileinfo_set_modified`, `xfileinfo_get_modified`, `fileinfo_get_modified`, `xfileinfo_set_file_type`, `fileinfo_set_file_type`, `xfileinfo_get_file_type`, `fileinfo_get_file_type`, `xfileinfo_set_file_name`, `fileinfo_set_file_name`, `xfileinfo_get_file_name`, `fileinfo_get_file_name`, `xfileinfo_set_file_size`, `fileinfo_set_file_size`, `xfileinfo_get_file_size`, `fileinfo_get_file_size`, `xfileinfo_set_date`, `fileinfo_set_date`, `xfileinfo_get_date`, `fileinfo_get_date`, `xfileinfo_set_title`, `fileinfo_set_title`, `xfileinfo_get_title`, `fileinfo_get_title`

## `fontdbox.h`

Types: `fontdbox_font`, `fontdbox_object`, `fontdbox_action_about_to_be_shown`, `fontdbox_action_apply_font`, `fontdbox_flags`, `fontdbox_full`

Functions: `xfontdbox_get_window_id`, `fontdbox_get_window_id`, `xfontdbox_set_font`, `fontdbox_set_font`, `xfontdbox_get_font`, `fontdbox_get_font`, `xfontdbox_set_size`, `fontdbox_set_size`, `xfontdbox_get_size`, `fontdbox_get_size`, `xfontdbox_set_try_string`, `fontdbox_set_try_string`, `xfontdbox_get_try_string`, `fontdbox_get_try_string`, `xfontdbox_set_title`, `fontdbox_set_title`, `xfontdbox_get_title`, `fontdbox_get_title`

## `fontmenu.h`

Types: `fontmenu_object`, `fontmenu_action_about_to_be_shown`, `fontmenu_action_selection`, `fontmenu_flags`, `fontmenu_full`

Functions: `xfontmenu_set_font`, `fontmenu_set_font`, `xfontmenu_get_font`, `fontmenu_get_font`

## `frontend.h`

Types: none

Functions: `xfrontend_extended_cmd_line`, `xfrontend_free_cmd_line`

## `gadget.h`

Types: `gadget_header`, `gadget_object`, `gadget_object_base`, `gadget_extension`, `gadget_extension_list`, `gadget_extension_list_base`, `gadget_flags`, `gadget_feature`

Functions: `xgadget_get_flags`, `gadget_get_flags`, `xgadget_set_flags`, `gadget_set_flags`, `xgadget_set_help_message`, `gadget_set_help_message`, `xgadget_get_help_message`, `gadget_get_help_message`, `xgadget_get_icon_list`, `gadget_get_icon_list`, `xgadget_set_focus`, `gadget_set_focus`, `xgadget_get_type`, `gadget_get_type`, `xgadget_move_gadget`, `gadget_move_gadget`, `xgadget_get_bbox`, `gadget_get_bbox`

## `iconbar.h`

Types: `iconbar_object`, `iconbar_action_about_to_be_shown`, `iconbar_flags`, `iconbar_full`, `iconbar_set_button`

Functions: `xiconbar_get_icon_handle`, `iconbar_get_icon_handle`, `xiconbar_set_menu`, `iconbar_set_menu`, `xiconbar_get_menu`, `iconbar_get_menu`, `xiconbar_set_action`, `iconbar_set_action`, `xiconbar_get_action`, `iconbar_get_action`, `xiconbar_set_show`, `iconbar_set_show`, `xiconbar_get_show`, `iconbar_get_show`, `xiconbar_set_help_message`, `iconbar_set_help_message`, `xiconbar_get_help_message`, `iconbar_get_help_message`, `xiconbar_set_text`, `iconbar_set_text`, `xiconbar_get_text`, `iconbar_get_text`, `xiconbar_set_sprite`, `iconbar_set_sprite`, `xiconbar_get_sprite`, `iconbar_get_sprite`

## `keyboardshortcut.h`

Types: `keyboardshortcut_object`, `keyboardshortcut_list`, `keyboardshortcut_list_base`, `keyboardshortcut_flags`

Functions: none

## `label.h`

Types: `label_object`

Functions: none

## `labelledbox.h`

Types: `labelledbox_object`

Functions: none

## `menu.h`

Types: `menu_entry_object`, `menu_object`, `menu_object_base`, `menu_action_about_to_be_shown`, `menu_action_sub_menu`, `menu_flags`, `menu_entry_flags`, `menu_full`, `menu_show_flags`, `menu_add_flags`, `menu_add_at`

Functions: `xmenu_update_tree`, `xmenu_set_tick`, `menu_set_tick`, `xmenu_get_tick`, `menu_get_tick`, `xmenu_set_fade`, `menu_set_fade`, `xmenu_get_fade`, `menu_get_fade`, `xmenu_set_entry_text`, `menu_set_entry_text`, `xmenu_get_entry_text`, `menu_get_entry_text`, `xmenu_set_entry_sprite`, `menu_set_entry_sprite`, `xmenu_get_entry_sprite`, `menu_get_entry_sprite`, `xmenu_set_sub_menu_show`, `menu_set_sub_menu_show`, `xmenu_get_sub_menu_show`, `menu_get_sub_menu_show`, `xmenu_set_sub_menu_action`, `menu_set_sub_menu_action`, `xmenu_get_sub_menu_action`, `menu_get_sub_menu_action`, `xmenu_set_click_show`, `menu_set_click_show`, `xmenu_get_click_show`, `menu_get_click_show`, `xmenu_set_click_action`, `menu_set_click_action`, `xmenu_get_click_action`, `menu_get_click_action`, `xmenu_set_help_message`, `menu_set_help_message`, `xmenu_get_help_message`, `menu_get_help_message`, `xmenu_set_entry_help_message`, `menu_set_entry_help_message`, `xmenu_get_entry_help_message`, `menu_get_entry_help_message`, `xmenu_add_entry`, `menu_add_entry`, `xmenu_remove_entry`, `menu_remove_entry`, `xmenu_get_height`, `menu_get_height`, `xmenu_get_width`, `menu_get_width`, `xmenu_set_title`, `menu_set_title`, `xmenu_get_title`, `menu_get_title`

## `numberrange.h`

Types: `numberrange_object`, `numberrange_action_value_changed`, `numberrange_bounds_flags`

Functions: `xnumberrange_set_value`, `numberrange_set_value`, `xnumberrange_get_value`, `numberrange_get_value`, `xnumberrange_set_bounds`, `numberrange_set_bounds`, `xnumberrange_get_bounds`, `numberrange_get_bounds`, `xnumberrange_get_components`, `numberrange_get_components`

## `optionbutton.h`

Types: `optionbutton_object`, `optionbutton_action_state_changed`

Functions: `xoptionbutton_set_label`, `optionbutton_set_label`, `xoptionbutton_get_label`, `optionbutton_get_label`, `xoptionbutton_set_action`, `optionbutton_set_action`, `xoptionbutton_get_action`, `optionbutton_get_action`, `xoptionbutton_set_state`, `optionbutton_set_state`, `xoptionbutton_get_state`, `optionbutton_get_state`

## `popup.h`

Types: `popup_object`, `popup_action_about_to_be_shown`, `popup_full`

Functions: `xpopup_set_menu`, `popup_set_menu`, `xpopup_get_menu`, `popup_get_menu`

## `printdbox.h`

Types: `printdbox_object`, `printdbox_action_about_to_be_shown`, `printdbox_action_setup_about_to_be_shown`, `printdbox_action_save`, `printdbox_action_print`, `printdbox_flags`, `printdbox_full`

Functions: `xprintdbox_get_window_id`, `printdbox_get_window_id`, `xprintdbox_set_page_range`, `printdbox_set_page_range`, `xprintdbox_get_page_range`, `printdbox_get_page_range`, `xprintdbox_set_copies`, `printdbox_set_copies`, `xprintdbox_get_copies`, `printdbox_get_copies`, `xprintdbox_set_scale`, `printdbox_set_scale`, `xprintdbox_get_scale`, `printdbox_get_scale`, `xprintdbox_set_orientation`, `printdbox_set_orientation`, `xprintdbox_get_orientation`, `printdbox_get_orientation`, `xprintdbox_get_title`, `printdbox_get_title`, `xprintdbox_set_draft`, `printdbox_set_draft`, `xprintdbox_get_draft`, `printdbox_get_draft`

## `proginfo.h`

Types: `proginfo_object`, `proginfo_action_about_to_be_shown`, `proginfo_flags`, `proginfo_full`

Functions: `xproginfo_get_window_id`, `proginfo_get_window_id`, `xproginfo_set_version`, `proginfo_set_version`, `xproginfo_get_version`, `proginfo_get_version`, `xproginfo_set_licence_type`, `proginfo_set_licence_type`, `xproginfo_get_licence_type`, `proginfo_get_licence_type`, `xproginfo_set_title`, `proginfo_set_title`, `xproginfo_get_title`, `proginfo_get_title`

## `quit.h`

Types: `quit_object`, `quit_action_about_to_be_shown`, `quit_flags`, `quit_full`

Functions: `xquit_get_window_id`, `quit_get_window_id`, `xquit_set_message`, `quit_set_message`, `xquit_get_message`, `quit_get_message`, `xquit_set_title`, `quit_set_title`, `xquit_get_title`, `quit_get_title`

## `radiobutton.h`

Types: `radiobutton_object`, `radiobutton_action_state_changed`

Functions: `xradiobutton_set_label`, `radiobutton_set_label`, `xradiobutton_get_label`, `radiobutton_get_label`, `xradiobutton_set_action`, `radiobutton_set_action`, `xradiobutton_get_action`, `radiobutton_get_action`, `xradiobutton_set_state`, `radiobutton_set_state`, `xradiobutton_get_state`, `radiobutton_get_state`

## `saveas.h`

Types: `saveas_object`, `saveas_action_about_to_be_shown`, `saveas_action_save_to_file`, `saveas_action_fill_buffer`, `saveas_action_save_completed`, `saveas_flags`, `saveas_full`

Functions: `xsaveas_get_window_id`, `saveas_get_window_id`, `xsaveas_set_title`, `saveas_set_title`, `xsaveas_get_title`, `saveas_get_title`, `xsaveas_set_file_name`, `saveas_set_file_name`, `xsaveas_get_file_name`, `saveas_get_file_name`, `xsaveas_set_file_type`, `saveas_set_file_type`, `xsaveas_get_file_type`, `saveas_get_file_type`, `xsaveas_set_file_size`, `saveas_set_file_size`, `xsaveas_get_file_size`, `saveas_get_file_size`, `xsaveas_selection_available`, `saveas_selection_available`, `xsaveas_set_data_address`, `saveas_set_data_address`, `xsaveas_buffer_filled`, `saveas_buffer_filled`, `xsaveas_file_save_completed`, `saveas_file_save_completed`

## `scale.h`

Types: `scale_object`, `scale_action_about_to_be_shown`, `scale_action_apply_factor`, `scale_flags`, `scale_full`

Functions: `xscale_get_window_id`, `scale_get_window_id`, `xscale_set_value`, `scale_set_value`, `xscale_get_value`, `scale_get_value`, `xscale_set_bounds`, `scale_set_bounds`, `xscale_get_bounds`, `scale_get_bounds`, `xscale_set_title`, `scale_set_title`, `xscale_get_title`, `scale_get_title`

## `slider.h`

Types: `slider_object`, `slider_action_value_changed`, `slider_bounds_flags`

Functions: `xslider_set_value`, `slider_set_value`, `xslider_get_value`, `slider_get_value`, `xslider_set_bounds`, `slider_set_bounds`, `xslider_get_bounds`, `slider_get_bounds`, `xslider_set_colour`, `slider_set_colour`, `xslider_get_colour`, `slider_get_colour`

## `stringset.h`

Types: `stringset_object`, `stringset_action_value_changed`

Functions: `xstringset_set_available`, `stringset_set_available`, `xstringsetsetselected_string`, `stringsetsetselected_string`, `xstringsetsetselected_index`, `stringsetsetselected_index`, `xstringsetgetselected_string`, `stringsetgetselected_string`, `xstringsetgetselected_index`, `stringsetgetselected_index`, `xstringset_set_allowable`, `stringset_set_allowable`, `xstringset_get_components`, `stringset_get_components`

## `toolbox.h`

Types: `toolbox_o`, `toolbox_id`, `toolbox_full`, `toolbox_position`, `toolbox_block`, `toolbox_resource_file_object`, `toolbox_resource_file_object_base`, `toolbox_relocation`, `toolbox_relocation_table`, `toolbox_relocation_table_base`, `toolbox_relocatable_object`, `toolbox_resource_file`, `toolbox_resource_file_base`, `toolbox_action_list`, `toolbox_action_list_base`, `toolbox_event_pair`, `toolbox_event_pair_list`, `toolbox_event_pair_list_base`, `toolbox_message_pair`, `toolbox_message_pair_list`, `toolbox_message_pair_list_base`, `toolbox_action_pair`, `toolbox_action_pair_list`, `toolbox_action_pair_list_base`, `toolbox_pair_list`, `toolbox_action_interest`, `toolbox_action_error`, `toolbox_action_object_auto_created`, `toolbox_action`, `toolbox_message`, `toolbox_c`, `toolbox_class`, `toolbox_position_tag`, `toolbox_object_flags`, `toolbox_string_reference`, `toolbox_msg_reference`, `toolbox_create_flags`, `toolbox_delete_flags`, `toolbox_show_flags`, `toolbox_hide_flags`, `toolbox_get_info_flags`, `toolbox_info`, `toolbox_misc_op_flags`, `toolbox_handle_flags`, `toolbox_get_class_flags`, `toolbox_get_parent_flags`, `toolbox_get_ancestor_flags`, `toolbox_get_template_flags`, `toolbox_event_flags`, `toolbox_initialise_flags`, `toolbox_load_flags`, `toolbox_look_up_flags`, `toolbox_filter_type`, `toolbox_register_flags`

Functions: `xtoolbox_create_object`, `xtoolbox_delete_object`, `xtoolbox_show_object`, `toolbox_show_object`, `xtoolbox_hide_object`, `xtoolbox_get_object_info`, `xtoolbox_set_client_handle`, `xtoolbox_get_client_handle`, `xtoolbox_get_object_class`, `xtoolbox_get_parent`, `toolbox_get_parent`, `xtoolbox_get_ancestor`, `toolbox_get_ancestor`, `xtoolbox_get_template_name`, `toolbox_get_template_name`, `xtoolbox_raise_toolbox_event`, `xtoolboxgetsysinfo_task_name`, `toolboxgetsysinfo_task_name`, `xtoolboxgetsysinfo_message_trans_control_block`, `toolboxgetsysinfo_message_trans_control_block`, `xtoolboxgetsysinfo_dir_name`, `toolboxgetsysinfo_dir_name`, `xtoolboxgetsysinfo_task`, `toolboxgetsysinfo_task`, `xtoolboxgetsysinfo_sprite_area`, `toolboxgetsysinfo_sprite_area`, `xtoolbox_initialise`, `toolbox_initialise`, `xtoolbox_load_resources`, `xtoolbox_de_register_object_module`, `xtoolbox_template_look_up`, `xtoolbox_register_object_module`, `xtoolbox_register_pre_filter`, `xtoolbox_register_post_filter`, `toolbox_register_post_filter`, `xservice_toolbox_starting`, `service_toolbox_starting`, `xservice_toolbox_task_born`, `service_toolbox_task_born`, `xservice_toolbox_task_died`, `service_toolbox_task_died`, `xservice_window_deleted`, `service_window_deleted`

## `window.h`

Types: `window_object`, `window_action_show_object`, `window_action_about_to_be_shown`, `window_flags`, `window_gadget_flags`, `window_full`, `window_tool_bar_flags`, `window_mouse_state`

Functions: `xwindow_get_pointer_info`, `window_get_pointer_info`, `xwindow_wimp_to_toolbox`, `window_wimp_to_toolbox`, `xwindow_register_external`, `xwindow_deregister_external`, `xwindow_extract_gadget_info`, `window_extract_gadget_info`, `xwindow_get_wimp_handle`, `window_get_wimp_handle`, `xwindow_add_gadget`, `window_add_gadget`, `xwindow_remove_gadget`, `window_remove_gadget`, `xwindow_set_menu`, `window_set_menu`, `xwindow_get_menu`, `window_get_menu`, `xwindow_set_pointer`, `window_set_pointer`, `xwindow_get_pointer`, `window_get_pointer`, `xwindow_set_help_message`, `window_set_help_message`, `xwindow_get_help_message`, `window_get_help_message`, `xwindow_add_keyboard_shortcuts`, `window_add_keyboard_shortcuts`, `xwindow_remove_keyboard_shortcuts`, `window_remove_keyboard_shortcuts`, `xwindow_set_title`, `window_set_title`, `xwindow_get_title`, `window_get_title`, `xwindow_set_default_focus`, `window_set_default_focus`, `xwindow_get_default_focus`, `window_get_default_focus`, `xwindow_set_extent`, `window_set_extent`, `xwindow_get_extent`, `window_get_extent`, `xwindow_force_redraw`, `window_force_redraw`, `xwindow_set_tool_bars`, `window_set_tool_bars`, `xwindow_get_tool_bars`, `window_get_tool_bars`, `xservice_window_module_starting`, `service_window_module_starting`, `xservice_window_module_dying`, `service_window_module_dying`, `xservice_gadget_registered`, `service_gadget_registered`, `xservice_gadget_deregistered`, `service_gadget_deregistered`, `xservice_redrawing_window`, `service_redrawing_window`

## `windowsupportexternal.h`

Types: none

Functions: `xwindowsupportexternal_create_icon`, `windowsupportexternal_create_icon`, `xwindowsupportexternal_create_object`, `windowsupportexternal_create_object`, `xwindowsupportexternal_create_gadget`, `windowsupportexternal_create_gadget`, `xwindowsupportexternal_alloc`, `windowsupportexternal_alloc`, `xwindowsupportexternal_free`, `windowsupportexternal_free`, `xwindowsupportexternal_realloc`, `windowsupportexternal_realloc`

## `writablefield.h`

Types: `writablefield_object`, `writablefield_action_value_changed`

Functions: `xwritablefield_set_value`, `writablefield_set_value`, `xwritablefield_get_value`, `writablefield_get_value`, `xwritablefield_set_allowable`, `writablefield_set_allowable`, `xwritablefield_set_font`, `writablefield_set_font`

