# User OSLib components

Wimp, Draw, Font, JPEG, printing, task, and other desktop-facing User interfaces.

Public C headers are under `.../OSLib/User/h`. The matching `hdr/` directory contains the parallel assembler/DefMod interface names for the same logical components.

## `basictrans.h`

Types: none

Functions: `xbasictrans_help`, `basictrans_help`, `xbasictrans_error`, `xbasictrans_message`

## `colourpicker.h`

Types: `colourpicker_d`, `colourpicker_colour`, `colourpicker_colour_base`, `colourpicker_dialogue`, `colourpicker_dialogue_base`, `colourpicker_model`, `colourpicker_message_colour_choice`, `colourpicker_message_colour_choice_base`, `colourpicker_message_colour_changed`, `colourpicker_message_colour_changed_base`, `colourpicker_message_open_parent_request`, `colourpicker_message_close_dialogue_request`, `colourpicker_message_reset_colour_request`, `colourpicker_dialogue_flags`, `colourpicker_model_flags`, `colourpicker_colour_flags`, `colourpicker_open_flags`, `colourpicker_close_flags`, `colourpicker_update_flags`, `colourpicker_read_flags`, `colourpicker_set_flags`, `colourpicker_help_flags`

Functions: `xcolourpicker_register_model`, `xcolourpicker_deregister_model`, `xcolourpicker_open_dialogue`, `colourpicker_open_dialogue`, `xcolourpicker_close_dialogue`, `xcolourpicker_update_dialogue`, `xcolourpicker_read_dialogue`, `colourpicker_read_dialogue`, `xcolourpicker_set_colour`, `xcolourpicker_help_reply`, `xcolourpickermodelswi_colour_changed`, `colourpickermodelswi_colour_changed`, `xcolourpickermodelswi_colour_changed_by_dragging`, `colourpickermodelswi_colour_changed_by_dragging`, `xcolourpickermodelswi_claim_event`, `colourpickermodelswi_claim_event`, `xcolourpickermodelswi_release_event`, `colourpickermodelswi_release_event`, `xcolourpickermodelswi_process_key`, `colourpickermodelswi_process_key`, `xservice_colour_picker_loaded`, `service_colour_picker_loaded`

## `compressjpeg.h`

Types: `compressjpeg_tag`, `compressjpeg_parameters`

Functions: `xcompressjpeg_start`, `compressjpeg_start`, `xcompressjpeg_write_line`, `xcompressjpeg_finish`

## `dragasprite.h`

Types: `dragasprite_flags`

Functions: `xdragasprite_start`, `dragasprite_start`, `xdragasprite_stop`

## `draw.h`

Types: `draw_path_element`, `draw_line_style`, `draw_dash_pattern`, `draw_dash_pattern_base`, `draw_path`, `draw_tag`, `draw_fill_style`, `draw_join_style`, `draw_cap_style`, `draw_output_path`

Functions: `xdraw_process_path`, `draw_process_path`, `xdraw_fill`, `xdraw_stroke`, `draw_stroke`, `xdraw_stroke_path`, `draw_stroke_path`, `xdraw_flatten_path`, `xdraw_transform_path`, `draw_transform_path`

## `drawfile.h`

Types: `drawfile_font_def`, `drawfile_font_def_base`, `drawfile_text_style`, `drawfile_path_style`, `drawfile_font_table`, `drawfile_font_table_base`, `drawfile_text`, `drawfile_text_base`, `drawfile_path`, `drawfile_path_with_pattern`, `drawfile_sprite`, `drawfile_sprite_base`, `drawfile_group`, `drawfile_group_base`, `drawfile_tagged`, `drawfile_tagged_base`, `drawfile_text_column`, `drawfile_text_column_list`, `drawfile_text_column_list_base`, `drawfile_area_text`, `drawfile_area_text_base`, `drawfile_text_area`, `drawfile_options`, `drawfile_trfm_text`, `drawfile_trfm_text_base`, `drawfile_trfm_sprite`, `drawfile_trfm_sprite_base`, `drawfile_jpeg`, `drawfile_object`, `drawfile_diagram`, `drawfile_diagram_base`, `drawfile_render_state`, `drawfile_declare_fonts_state`, `drawfile_type`, `drawfile_path_style_flags`, `drawfile_text_flags`, `drawfile_render_flags`, `drawfile_declare_fonts_flags`, `draw_paper_options`, `draw_entry_mode`, `drawfile_bbox_flags`

Functions: `xdrawfile_render`, `drawfile_render`, `xdrawfile_bbox`, `drawfile_bbox`, `xdrawfile_declare_fonts`, `xservice_draw_object_render`, `service_draw_object_render`, `xservice_draw_object_declare_fonts`, `service_draw_object_declare_fonts`

## `filter.h`

Types: none

Functions: `xfilter_register_pre_filter`, `xfilter_register_post_filter`, `filter_register_post_filter`, `xfilter_de_register_pre_filter`, `xfilter_de_register_post_filter`, `filter_de_register_post_filter`, `xservice_filter_manager_installed`, `service_filter_manager_installed`, `xservice_filter_manager_dying`, `service_filter_manager_dying`

## `font.h`

Types: `font_paint_block`, `font_scan_block`, `font_thresholds`, `font_thresholds_base`, `font_colour_table`, `font_colour_table_base`, `font_bbox_info`, `font_width_info`, `font_misc_info`, `font_long_kern_pair`, `font_kern_info`, `font_string_flags`, `font_f`, `font_bitmap_type`, `font_characteristic_flags`, `font_list_context`, `font_kern_flags`, `font_metric_flags`, `font_short_kern_pair`, `font_decode_flags`

Functions: `xfont_cache_addr`, `font_cache_addr`, `xfont_find_font`, `font_find_font`, `xfont_lose_font`, `xfont_read_defn`, `font_read_defn`, `xfont_read_identifier`, `font_read_identifier`, `xfont_read_info`, `font_read_info`, `xfont_string_width`, `font_string_width`, `xfont_paint`, `font_paint`, `xfont_caret`, `font_caret`, `xfont_convertto_os`, `font_convertto_os`, `xfont_converttopoints`, `font_converttopoints`, `xfont_set_font`, `xfont_current_font`, `font_current_font`, `xfont_future_font`, `font_future_font`, `xfont_find_caret`, `font_find_caret`, `xfont_char_bbox`, `font_char_bbox`, `xfont_read_scale_factor`, `font_read_scale_factor`, `xfont_set_scale_factor`, `font_set_scale_factor`, `xfont_list_fonts`, `font_list_fonts`, `xfont_set_font_colours`, `xfont_set_palette`, `font_set_palette`, `xfont_set_true_palette`, `font_set_true_palette`, `xfont_read_thresholds`, `font_read_thresholds`, `xfont_set_thresholds`, `font_set_thresholds`, `xfont_find_caretj`, `font_find_caretj`, `xfont_string_bbox`, `font_string_bbox`, `xfont_read_colour_table`, `font_read_colour_table`, `xfont_make_bitmap`, `font_make_bitmap`, `xfont_un_cache_file`, `xfont_set_font_max`, `font_set_font_max`, `xfont_read_font_max`, `font_read_font_max`, `xfont_read_font_prefix`, `font_read_font_prefix`, `xfont_switch_output_to_buffer`, `font_switch_output_to_buffer`, `xfont_read_font_metrics`, `font_read_font_metrics`, `xfont_decode_menu`, `font_decode_menu`, `xfont_scan_string`, `font_scan_string`, `xfont_current_rgb`, `font_current_rgb`, `xfont_future_rgb`, `font_future_rgb`, `xfont_read_encoding_filename`, `font_read_encoding_filename`, `xfont_find_field`, `font_find_field`, `xfont_apply_fields`, `font_apply_fields`, `xfont_lookup_font`, `font_lookup_font`, `xservice_fonts_changed`, `service_fonts_changed`

## `help.h`

Types: `help_message_request`, `help_message_reply`

Functions: none

## `hourglass.h`

Types: none

Functions: `xhourglass_on`, `xhourglass_off`, `xhourglass_smash`, `xhourglass_start`, `xhourglass_percentage`, `xhourglass_leds`, `xhourglass_colours`, `hourglass_colours`

## `jpeg.h`

Types: `jpeg_image`, `jpeg_image_base`, `jpeg_info_flags`, `jpeg_scale_flags`, `jpeg_transform_flags`

Functions: `xjpeginfo_dimensions`, `jpeginfo_dimensions`, `xjpegfileinfo_dimensions`, `jpegfileinfo_dimensions`, `xjpeg_plot_scaled`, `jpeg_plot_scaled`, `xjpeg_plot_scaled_colour_map`, `jpeg_plot_scaled_colour_map`, `xjpeg_plot_file_scaled`, `jpeg_plot_file_scaled`, `xjpeg_plot_file_scaled_colour_map`, `jpeg_plot_file_scaled_colour_map`, `xjpeg_plot_transformed`, `xjpeg_plot_transformed_colour_map`, `jpeg_plot_transformed_colour_map`, `xjpeg_plot_file_transformed`, `xjpeg_plot_file_transformed_colour_map`

## `pdriver.h`

Types: `pdriver_message_print_error`, `pdriver_message_print_type_odd`, `pdriver_message_ps_printer_query`, `pdriver_type`, `pdriver_features`, `pdriver_font_flags`, `pdriver_font_map_flags`, `pdriver_font_add_flags`, `pdriver_enumerate_flags`

Functions: `xpdriver_info`, `pdriver_info`, `xpdriver_set_info`, `pdriver_set_info`, `xpdriver_check_features`, `xpdriver_page_size`, `pdriver_page_size`, `xpdriver_set_page_size`, `pdriver_set_page_size`, `xpdriver_select_job`, `pdriver_select_job`, `xpdriver_current_job`, `xpdriver_end_job`, `xpdriver_abort_job`, `xpdriver_reset`, `xpdriver_give_rectangle`, `pdriver_give_rectangle`, `xpdriver_draw_page`, `pdriver_draw_page`, `xpdriver_get_rectangle`, `pdriver_get_rectangle`, `xpdriver_cancel_job`, `xpdriver_screen_dump`, `xpdriver_enumerate_jobs`, `xpdriver_cancel_job_with_error`, `xpdriver_select_illustration`, `xpdriver_insert_illustration`, `pdriver_insert_illustration`, `xpdriver_declare_font`, `xpdriver_declare_driver`, `xpdriver_remove_driver`, `xpdriver_select_driver`, `xpdriver_enumerate_drivers`, `pdriver_enumerate_drivers`, `xpdrivermiscop_add_font`, `pdrivermiscop_add_font`, `xpdrivermiscop_remove_font`, `pdrivermiscop_remove_font`, `xpdrivermiscop_enumerate_fonts`, `pdrivermiscop_enumerate_fonts`, `xpdrivermiscop_register_dumper`, `pdrivermiscop_register_dumper`, `xpdrivermiscop_deregister_dumper`, `pdrivermiscop_deregister_dumper`, `xpdrivermiscop_strip_types`, `pdrivermiscop_strip_types`, `xpdrivermiscopfordriver_add_font`, `pdrivermiscopfordriver_add_font`, `xpdrivermiscopfordriver_remove_font`, `pdrivermiscopfordriver_remove_font`, `xpdrivermiscopfordriver_enumerate_fonts`, `pdrivermiscopfordriver_enumerate_fonts`, `xpdrivermiscopfordriver_register_dumper`, `pdrivermiscopfordriver_register_dumper`, `xpdrivermiscopfordriver_deregister_dumper`, `pdrivermiscopfordriver_deregister_dumper`, `xpdrivermiscopfordriver_strip_types`, `pdrivermiscopfordriver_strip_types`, `xpdriver_set_driver`, `pdriver_set_driver`, `xservice_print`, `service_print`, `xservice_pdriver_starting`, `service_pdriver_starting`, `xservice_pdriver_get_messages`, `service_pdriver_get_messages`, `xservice_pdriver_changed`, `service_pdriver_changed`

## `pdumper.h`

Types: `pdumper_job_flags`, `pdumper_device`, `pdumper_strip_type`, `pdumper_features`, `pdumper_format`, `pdumper_halftone_flags`

Functions: `xpdumper_info`, `pdumper_info`, `xpdumper_claim`, `pdumper_claim`, `xpdumper_free`, `pdumper_free`, `xpdumper_find`, `pdumper_find`, `xpdumper_start_job`, `xpdumper_tidy_job`, `pdumper_tidy_job`, `xpdumper_set_colour`, `pdumper_set_colour`, `xpdumper_prepare_strip`, `pdumper_prepare_strip`, `xpdumper_lookup_error`, `xpdumper_copy_filename`, `xservice_pdumper_starting`, `service_pdumper_starting`, `xservice_pdumper_dying`, `service_pdumper_dying`

## `taskmanager.h`

Types: `taskmanager_task`, `taskmanager_flags`, `taskmanager_shutdown_flags`

Functions: `xtaskmanager_task_name_from_handle`, `xtaskmanager_enumerate_tasks`, `taskmanager_enumerate_tasks`, `xtaskmanager_shutdown`

## `taskwindow.h`

Types: `taskwindow_message_data`, `taskwindow_message_ego`, `taskwindow_message_new_task`

Functions: `xtaskwindowtaskinfo_window_task`, `taskwindowtaskinfo_window_task`, `xupcall_sleep`, `upcall_sleep`

## `wimp.h`

Types: `wimp_w`, `wimp_t`, `wimp_icon_data`, `wimp_icon`, `wimp_icon_create`, `wimp_window`, `wimp_window_base`, `wimp_window_state`, `wimp_icon_state`, `wimp_window_info`, `wimp_window_info_base`, `wimp_outline`, `wimp_draw`, `wimp_open`, `wimp_close`, `wimp_leaving`, `wimp_entering`, `wimp_pointer`, `wimp_dragged`, `wimp_key`, `wimp_selection`, `wimp_scroll`, `wimp_pollword`, `wimp_drag`, `wimp_caret`, `wimp_menu_entry`, `wimp_menu`, `wimp_menu_base`, `wimp_message_data_xfer`, `wimp_message_ram_xfer`, `wimp_message_prequit`, `wimp_message_save_desktop`, `wimp_message_device`, `wimp_message_data_saved`, `wimp_message_shutdown`, `wimp_message_claim_entity`, `wimp_message_data_request`, `wimp_message_dragging`, `wimp_message_drag_claim`, `wimp_message_menu_warning`, `wimp_message_task_initialise`, `wimp_message_slot_size`, `wimp_message_set_slot`, `wimp_message_task_name_rq`, `wimp_message_task_name_is`, `wimp_message_menus_deleted`, `wimp_message_iconise`, `wimp_message_window_closed`, `wimp_message_window_info`, `wimp_message_font_changed`, `wimp_message`, `wimp_block`, `wimp_message_list`, `wimp_message_list_base`, `wimp_i`, `wimp_colour`, `wimp_version_no`, `wimp_event_no`, `wimp_poll_flags`, `wimp_window_flags`, `wimp_icon_flags`, `wimp_menu_flags`, `wimp_mouse_state`, `wimp_drag_type`, `wimp_key_no`, `wimp_error_box_flags`, `wimp_error_box_selection`, `wimp_pre_quit_flags`, `wimp_save_desktop_flags`, `wimp_shutdown_flags`, `wimp_claim_flags`, `wimp_data_request_flags`, `wimp_dragging_flags`, `wimp_drag_claim_flags`, `wimp_priority`, `wimp_menu_state_flags`, `wimptextop_paint_flags`

Functions: `xwimp_initialise`, `wimp_initialise`, `xwimp_create_window`, `wimp_create_window`, `xwimp_create_icon`, `wimp_create_icon`, `xwimp_create_icon_relative`, `xwimp_create_icon_prioritised`, `xwimp_delete_window`, `wimp_delete_window`, `xwimp_delete_icon`, `wimp_delete_icon`, `xwimp_open_window`, `wimp_open_window`, `xwimp_close_window`, `wimp_close_window`, `xwimp_poll`, `wimp_poll`, `xwimp_redraw_window`, `wimp_redraw_window`, `xwimp_update_window`, `wimp_update_window`, `xwimp_get_rectangle`, `wimp_get_rectangle`, `xwimp_get_window_state`, `wimp_get_window_state`, `xwimp_get_window_info`, `wimp_get_window_info`, `xwimp_get_window_info_header_only`, `wimp_get_window_info_header_only`, `xwimp_set_icon_state`, `wimp_set_icon_state`, `xwimp_get_icon_state`, `wimp_get_icon_state`, `xwimp_get_pointer_info`, `wimp_get_pointer_info`, `xwimp_drag_box`, `wimp_drag_box`, `xwimp_force_redraw`, `wimp_force_redraw`, `xwimp_set_caret_position`, `wimp_set_caret_position`, `xwimp_get_caret_position`, `wimp_get_caret_position`, `xwimp_create_menu`, `wimp_create_menu`, `xwimp_decode_menu`, `wimp_decode_menu`, `xwimp_which_icon`, `xwimp_set_extent`, `xwimp_set_pointer_shape`, `wimp_set_pointer_shape`, `xwimp_open_template`, `wimp_open_template`, `xwimp_close_template`, `xwimp_load_template`, `wimp_load_template`, `xwimp_process_key`, `xwimp_close_down`, `wimp_close_down`, `xwimp_start_task`, `xwimp_report_error`, `wimp_report_error`, `xwimp_report_error_by_category`, `wimp_report_error_by_category`, `xwimp_get_window_outline`, `wimp_get_window_outline`, `xwimp_poll_idle`, `xwimp_plot_icon`, `wimp_plot_icon`, `xwimp_set_mode`, `xwimp_set_palette`, `wimp_set_palette`, `xwimp_read_palette`, `wimp_read_palette`, `xwimp_read_true_palette`, `wimp_read_true_palette`, `xwimp_set_colour`, `xwimp_send_message`, `xwimp_send_message_to_window`, `wimp_send_message_to_window`, `xwimp_create_sub_menu`, `wimp_create_sub_menu`, `xwimp_base_of_sprites`, `wimp_base_of_sprites`, `xwimp_block_copy`, `wimp_block_copy`, `xwimp_slot_size`, `wimp_slot_size`, `xwimp_read_pix_trans`, `wimp_read_pix_trans`, `xwimpclaimfreememory_alloc`, `wimpclaimfreememory_alloc`, `xwimpclaimfreememory_free`, `wimpclaimfreememory_free`, `xwimp_command_window`, `xwimp_text_colour`, `xwimp_transfer_block`, `wimp_transfer_block`, `xwimp_set_font_colours`, `wimp_set_font_colours`, `xwimp_get_menu_state`, `xwimp_register_filter`, `xwimp_add_messages`, `xwimp_remove_messages`, `xwimp_set_colour_mapping`, `wimp_set_colour_mapping`, `xwimptextop_set_colour`, `wimptextop_set_colour`, `xwimptextop_string_width`, `wimptextop_string_width`, `xwimptextop_paint`, `wimptextop_paint`, `xwimp_set_watchdog_state`, `xwimp_resize_icon`, `wimp_resize_icon`, `xservice_memory`, `service_memory`, `xservice_start_wimp`, `service_start_wimp`, `xservice_started_wimp`, `service_started_wimp`, `xservice_mouse_trap`, `service_mouse_trap`, `xservice_wimp_close_down`, `service_wimp_close_down`, `xservice_wimp_report_error`, `service_wimp_report_error`, `xservice_wimp_save_desktop`, `service_wimp_save_desktop`, `xservice_wimp_palette`, `service_wimp_palette`, `xservice_desktop_welcome`, `service_desktop_welcome`, `xservice_shut_down`, `service_shut_down`, `xservice_shut_down_complete`, `service_shut_down_complete`, `xservice_wimp_sprites_moved`, `service_wimp_sprites_moved`, `xservice_wimp_register_filters`, `service_wimp_register_filters`, `xservice_error_starting`, `service_error_starting`, `xservice_error_button_pressed`, `service_error_button_pressed`, `xservice_error_ending`, `service_error_ending`

## `wimpreadsysinfo.h`

Types: `wimpreadsysinfo_state`, `wimpreadsysinfo_direction`

Functions: `xwimpreadsysinfo_task_count`, `wimpreadsysinfo_task_count`, `xwimpreadsysinfo_wimp_mode`, `wimpreadsysinfo_wimp_mode`, `xwimpreadsysinfo_sprite_suffix`, `wimpreadsysinfo_sprite_suffix`, `xwimpreadsysinfo_desktop_state`, `wimpreadsysinfo_desktop_state`, `xwimpreadsysinfo_write_dir`, `wimpreadsysinfo_write_dir`, `xwimpreadsysinfo_task`, `wimpreadsysinfo_task`, `xwimpreadsysinfo_version`, `wimpreadsysinfo_version`, `xwimpreadsysinfo_font`, `wimpreadsysinfo_font`, `xwimpreadsysinfo_tool_sprites`, `wimpreadsysinfo_tool_sprites`, `xwimpreadsysinfo_application_limit`, `wimpreadsysinfo_application_limit`

## `wimpspriteop.h`

Types: none

Functions: `xwimpspriteop_merge_sprite_file`, `wimpspriteop_merge_sprite_file`, `xwimpspriteop_get_sprite`, `wimpspriteop_get_sprite`, `xwimpspriteop_select_sprite`, `wimpspriteop_select_sprite`, `xwimpspriteop_put_sprite`, `wimpspriteop_put_sprite`, `xwimpspriteop_put_sprite_user_coords`, `wimpspriteop_put_sprite_user_coords`, `xwimpspriteop_set_pointer_shape`, `wimpspriteop_set_pointer_shape`, `xwimpspriteop_read_palette_size`, `wimpspriteop_read_palette_size`, `xwimpspriteop_read_sprite_size`, `wimpspriteop_read_sprite_size`, `xwimpspriteop_read_pixel_colour`, `wimpspriteop_read_pixel_colour`, `xwimpspriteop_read_pixel_mask`, `wimpspriteop_read_pixel_mask`, `xwimpspriteop_plot_mask`, `wimpspriteop_plot_mask`, `xwimpspriteop_plot_mask_user_coords`, `wimpspriteop_plot_mask_user_coords`, `xwimpspriteop_plot_mask_scaled`, `wimpspriteop_plot_mask_scaled`, `xwimpspriteop_put_sprite_scaled`, `wimpspriteop_put_sprite_scaled`, `xwimpspriteop_put_sprite_grey_scaled`, `wimpspriteop_put_sprite_grey_scaled`, `xwimpspriteop_plot_mask_trfm`, `wimpspriteop_plot_mask_trfm`, `xwimpspriteop_put_sprite_trfm`, `wimpspriteop_put_sprite_trfm`

