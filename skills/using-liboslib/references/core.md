# Core OSLib components

Core SWI wrappers, OS types, ColourTrans, MessageTrans, SpriteOp, memory, module, and territory interfaces.

Public C headers are under `.../OSLib/Core/h`. The matching `hdr/` directory contains the parallel assembler/DefMod interface names for the same logical components.

## `buffer.h`

Types: `buffer_b`, `buffer_internal_id`, `buffer_mouse_data`, `buffer_no`, `buffer_flags`

Functions: `xbuffer_create`, `xbuffer_remove`, `xbuffer_register`, `xbuffer_deregister`, `xbuffer_modify_flags`, `xbuffer_link_device`, `buffer_link_device`, `xbuffer_unlink_device`, `xbuffer_get_info`, `buffer_get_info`, `xbuffer_threshold`, `buffer_threshold`, `xbuffer_internal_info`, `buffer_internal_info`, `xinsv`, `insv`, `xinsv_block`, `insv_block`, `xremv`, `remv`, `xremv_block`, `remv_block`, `xcnpv`, `cnpv`, `xservice_buffer_starting`, `service_buffer_starting`, `xevent_output_buffer_empty`, `event_output_buffer_empty`, `xevent_input_buffer_full`, `event_input_buffer_full`, `xevent_input_buffer_full_block_op`, `event_input_buffer_full_block_op`, `xupcall_buffer_filling`, `upcall_buffer_filling`, `xupcall_buffer_emptying`, `upcall_buffer_emptying`

## `cache.h`

Types: none

Functions: `xcache_control`, `xcache_cacheable`, `xcache_updateable`, `xcache_disruptive`, `xcache_flush`

## `colourtrans.h`

Types: `colourtrans_gcol_list`, `colourtrans_gcol_list_base`, `colourtrans_calibration_table`, `colourtrans_calibration_table_base`, `colourtrans_gcol_flags`, `colourtrans_table_flags`, `colourtrans_calibration_flags`, `colourtrans_palette_flags`, `colourtrans_colour_flags`, `colourtrans_text_colour_flags`

Functions: `xcolourtrans_select_table`, `colourtrans_select_table`, `xcolourtrans_select_table_for_sprite`, `colourtrans_select_table_for_sprite`, `xcolourtrans_select_gcol_table`, `colourtrans_select_gcol_table`, `xcolourtrans_select_gcol_table_for_sprite`, `colourtrans_select_gcol_table_for_sprite`, `xcolourtrans_return_gcol`, `xcolourtrans_set_gcol`, `colourtrans_set_gcol`, `xcolourtrans_return_colour_number`, `xcolourtrans_return_gcol_for_mode`, `xcolourtrans_return_colour_number_for_mode`, `xcolourtrans_return_opp_gcol`, `xcolourtrans_set_opp_gcol`, `colourtrans_set_opp_gcol`, `xcolourtrans_return_opp_colour_number`, `xcolourtrans_return_opp_gcol_for_mode`, `xcolourtrans_return_opp_colour_number_for_mode`, `xcolourtrans_gcol_to_colour_number`, `xcolourtrans_colour_number_to_gcol`, `xcolourtrans_return_font_colours`, `colourtrans_return_font_colours`, `xcolourtrans_set_font_colours`, `colourtrans_set_font_colours`, `xcolourtrans_invalidate_cache`, `xcolourtrans_set_calibration`, `xcolourtrans_read_calibration`, `colourtrans_read_calibration`, `xcolourtrans_convert_device_colour`, `colourtrans_convert_device_colour`, `xcolourtrans_convert_device_palette`, `xcolourtrans_convert_rgb_to_cie`, `colourtrans_convert_rgb_to_cie`, `xcolourtrans_convert_cie_to_rgb`, `colourtrans_convert_cie_to_rgb`, `xcolourtrans_write_calibration_to_file`, `xcolourtrans_convert_rgb_to_hsv`, `colourtrans_convert_rgb_to_hsv`, `xcolourtrans_convert_hsv_to_rgb`, `colourtrans_convert_hsv_to_rgb`, `xcolourtrans_convert_rgb_to_cmyk`, `colourtrans_convert_rgb_to_cmyk`, `xcolourtrans_convert_cmyk_to_rgb`, `colourtrans_convert_cmyk_to_rgb`, `xcolourtrans_read_palette`, `colourtrans_read_palette`, `xcolourtrans_write_palette`, `colourtrans_write_palette`, `xcolourtrans_set_colour`, `colourtrans_set_colour`, `xcolourtransmiscop_set_weights`, `colourtransmiscop_set_weights`, `xcolourtrans_write_loadings_to_file`, `colourtrans_write_loadings_to_file`, `xcolourtrans_set_text_colour`, `colourtrans_set_text_colour`, `xcolourtrans_set_opp_text_colour`, `colourtrans_set_opp_text_colour`, `xcolourtrans_generate_table`, `colourtrans_generate_table`, `xcolourtrans_generate_table_for_sprite`, `colourtrans_generate_table_for_sprite`, `xservice_calibration_changed`, `service_calibration_changed`, `xservice_invalidate_cache`, `service_invalidate_cache`

## `debugger.h`

Types: none

Functions: `xdebugger_disassemble`, `debugger_disassemble`

## `dma.h`

Types: `dma_c`, `dma_tag`, `dma_routines`, `dma_scatter`, `dma_scatter_list`, `dma_scatter_list_base`, `dma_register_channel_flags`, `dma_queue_flags`, `dma_suspend_flags`, `dma_resume_flags`, `dma_examine_flags`

Functions: `xdma_register_channel`, `dma_register_channel`, `xdma_deregister_channel`, `xdma_queue_transfer`, `dma_queue_transfer`, `xdma_terminate_transfer`, `xdma_suspend_transfer`, `xdma_resume_transfer`, `xdma_examine_transfer`

## `fpemulator.h`

Types: none

Functions: `xfpemulator_version`

## `iic.h`

Types: none

Functions: `xiiccontrol_read`, `iiccontrol_read`, `xiiccontrol_write`, `iiccontrol_write`

## `macros.h`

Types: none

Functions: none

## `messagetrans.h`

Types: `messagetrans_control_block`, `messagetrans_file_flags`

Functions: `xmessagetrans_file_info`, `messagetrans_file_info`, `xmessagetrans_open_file`, `xmessagetrans_lookup`, `messagetrans_lookup`, `xmessagetrans_make_menus`, `messagetrans_make_menus`, `xmessagetrans_close_file`, `xmessagetrans_enumerate_tokens`, `messagetrans_enumerate_tokens`, `xmessagetrans_error_lookup`, `messagetrans_error_lookup`, `xmessagetrans_gs_lookup`, `messagetrans_gs_lookup`, `xmessagetrans_copy_error`, `xmessagetrans_dictionary`, `xservice_message_file_closed`, `service_message_file_closed`

## `os.h`

Types: `os_mode`, `os_colour_pair`, `os_palette`, `os_palette_base`, `os_sprite_palette`, `os_sprite_palette_base`, `os_ecf`, `os_correction_table`, `os_bcd_date_and_time`, `os_station_number`, `os_box`, `os_factors`, `os_change_box`, `os_error`, `os_coord`, `os_trfm`, `os_hom_trfm`, `os_pgm`, `os_error_handler_buffer`, `os_colour_map`, `os_register_block`, `os_vdu_var_list`, `os_vdu_var_list_base`, `os_key_handler`, `os_key_handler_base`, `os_gi`, `os_gs`, `os_gs_base`, `os_mem_map_request`, `os_mem_map_request_list`, `os_mem_map_request_list_base`, `os_page_block`, `pointerv_record`, `os_mode_block`, `os_mode_block_base`, `os_mode_selector`, `os_mode_selector_base`, `os_t`, `os_f`, `os_gcol`, `os_tint`, `os_action`, `os_colour`, `os_colour_number`, `os_plot_code`, `os_var_type`, `os_mode_var`, `os_mode_flags`, `os_vdu_var`, `os_device_type`, `os_read_unsigned_flags`, `os_gs_flags`, `os_dynamic_area_no`, `keyv_type`, `os_handler_type`, `os_sort_type`, `os_area_flags`, `os_changed_box_state`, `os_colour_flags`, `os_pointer_type`, `osmemory_flags`, `osmemory_type_flags`, `osmemory_controller_flags`

Functions: `xos_writec`, `xwrchv`, `wrchv`, `xos_write0`, `xos_new_line`, `xos_readc`, `os_readc`, `xrdchv`, `rdchv`, `xos_cli`, `xcliv`, `cliv`, `xos_read_line`, `os_read_line`, `xos_read_line_given_echo`, `os_read_line_given_echo`, `xos_read_line_suppress_invalid`, `os_read_line_suppress_invalid`, `xos_read_line_given_echo_suppress_invalid`, `os_read_line_given_echo_suppress_invalid`, `xreadlinev`, `readlinev`, `xos_control`, `os_control`, `xos_get_env`, `os_get_env`, `xos_exit`, `os_exit`, `xos_set_env`, `os_set_env`, `xos_call_back`, `os_call_back`, `xos_break_pt`, `xos_break_ctrl`, `os_break_ctrl`, `xos_unused_swi`, `xos_update_memc`, `xos_set_call_back`, `xos_mouse`, `os_mouse`, `xmousev`, `mousev`, `xos_claim`, `xos_release`, `xos_read_unsigned`, `os_read_unsigned`, `xos_read_var_val`, `os_read_var_val`, `xos_set_var_val`, `os_set_var_val`, `xos_gs_init`, `os_gs_init`, `xos_gs_read`, `os_gs_read`, `xos_gs_trans`, `os_gs_trans`, `xos_binary_to_decimal`, `os_binary_to_decimal`, `xos_change_dynamic_area`, `os_change_dynamic_area`, `xos_generate_error`, `xerrorv`, `errorv`, `xos_read_escape_state`, `os_read_escape_state`, `xos_evaluate_expression`, `os_evaluate_expression`, `xos_read_palette`, `os_read_palette`, `xpalettev_read_entry`, `palettev_read_entry`, `xpalettev_set_entry`, `palettev_set_entry`, `xpalettev_set_on`, `palettev_set_on`, `xpalettev_set_off`, `palettev_set_off`, `xpalettev_default`, `palettev_default`, `xpalettev_read_entries`, `palettev_read_entries`, `xpalettev_write_entries`, `palettev_write_entries`, `xpalettev_set_gamma_corrections`, `palettev_set_gamma_corrections`, `xos_read_vdu_variables`, `xos_read_point`, `os_read_point`, `xos_read_mode_variable`, `os_read_mode_variable`, `xos_remove_cursors`, `xos_restore_cursors`, `xos_swi_number_to_string`, `os_swi_number_to_string`, `xos_swi_number_from_string`, `os_swi_number_from_string`, `xos_validate_address`, `os_validate_address`, `xos_call_after`, `xos_call_every`, `xos_remove_ticker_event`, `xtickerv`, `tickerv`, `xos_install_key_handler`, `xkeyv_present`, `keyv_present`, `xkeyv_transition_up`, `keyv_transition_up`, `xkeyv_transition_down`, `keyv_transition_down`, `xkeyv_led_state`, `keyv_led_state`, `xkeyv_enable_drivers`, `keyv_enable_drivers`, `xos_check_mode_valid`, `os_check_mode_valid`, `xos_change_environment`, `os_change_environment`, `xchangeenvironmentv`, `changeenvironmentv`, `xosclaimscreenmemory_alloc`, `osclaimscreenmemory_alloc`, `xosclaimscreenmemory_free`, `osclaimscreenmemory_free`, `xos_read_monotonic_time`, `xos_substitute_args`, `os_substitute_args`, `xos_pretty_print`, `xos_plot`, `xukplotv`, `ukplotv`, `xos_writen`, `xos_add_to_vector`, `xos_write_env`, `xos_read_args`, `os_read_args`, `xos_read_ram_fs_limits`, `os_read_ram_fs_limits`, `xos_claim_device_vector`, `os_claim_device_vector`, `xos_release_device_vector`, `os_release_device_vector`, `xos_delink_application`, `os_delink_application`, `xos_relink_application`, `xos_heap_sort`, `os_heap_sort`, `xos_exit_and_die`, `os_exit_and_die`, `xos_read_mem_map_info`, `os_read_mem_map_info`, `xos_read_mem_map_entries`, `xos_set_mem_map_entries`, `xos_add_call_back`, `xos_read_default_handler`, `os_read_default_handler`, `xos_set_ecf_origin`, `xos_confirm`, `os_confirm`, `xos_changed_box`, `os_changed_box`, `xos_crc`, `xos_read_dynamic_area`, `os_read_dynamic_area`, `xos_print_char`, `xos_change_redirection`, `os_change_redirection`, `xos_remove_call_back`, `xos_find_mem_map_entries`, `xos_set_colour`, `xos_read_colour`, `os_read_colour`, `xospointer_get`, `ospointer_get`, `xospointer_set`, `ospointer_set`, `xpointerv_status`, `pointerv_status`, `xpointerv_enumerate`, `pointerv_enumerate`, `xpointerv_selected`, `pointerv_selected`, `xosscreenmode_select`, `osscreenmode_select`, `xosscreenmode_current`, `osscreenmode_current`, `xosscreenmode_enumerate`, `osscreenmode_enumerate`, `xosdynamicarea_create`, `osdynamicarea_create`, `xosdynamicarea_delete`, `osdynamicarea_delete`, `xosdynamicarea_read`, `osdynamicarea_read`, `xosdynamicarea_enumerate`, `osdynamicarea_enumerate`, `xosdynamicarea_renumber`, `osdynamicarea_renumber`, `xosmemory_page_op`, `osmemory_page_op`, `xosmemory_read_arrangement_table_size`, `osmemory_read_arrangement_table_size`, `xosmemory_read_arrangement_table`, `osmemory_read_arrangement_table`, `xosmemory_read_size`, `osmemory_read_size`, `xosmemory_read_controller`, `osmemory_read_controller`, `xosclaimprocessorvector_alloc`, `osclaimprocessorvector_alloc`, `xosclaimprocessorvector_free`, `osclaimprocessorvector_free`, `xos_reset`, `xos_mmu_control`, `os_mmu_control`, `xos_convert_standard_date_and_time`, `os_convert_standard_date_and_time`, `xos_convert_date_and_time`, `os_convert_date_and_time`, `xos_convert_hex1`, `os_convert_hex1`, `xos_convert_hex2`, `os_convert_hex2`, `xos_convert_hex4`, `os_convert_hex4`, `xos_convert_hex6`, `os_convert_hex6`, `xos_convert_hex8`, `os_convert_hex8`, `xos_convert_cardinal1`, `os_convert_cardinal1`, `xos_convert_cardinal2`, `os_convert_cardinal2`, `xos_convert_cardinal3`, `os_convert_cardinal3`, `xos_convert_cardinal4`, `os_convert_cardinal4`, `xos_convert_integer1`, `os_convert_integer1`, `xos_convert_integer2`, `os_convert_integer2`, `xos_convert_integer3`, `os_convert_integer3`, `xos_convert_integer4`, `os_convert_integer4`, `xos_convert_binary1`, `os_convert_binary1`, `xos_convert_binary2`, `os_convert_binary2`, `xos_convert_binary3`, `os_convert_binary3`, `xos_convert_binary4`, `os_convert_binary4`, `xos_convert_spaced_cardinal1`, `os_convert_spaced_cardinal1`, `xos_convert_spaced_cardinal2`, `os_convert_spaced_cardinal2`, `xos_convert_spaced_cardinal3`, `os_convert_spaced_cardinal3`, `xos_convert_spaced_cardinal4`, `os_convert_spaced_cardinal4`, `xos_convert_spaced_integer1`, `os_convert_spaced_integer1`, `xos_convert_spaced_integer2`, `os_convert_spaced_integer2`, `xos_convert_spaced_integer3`, `os_convert_spaced_integer3`, `xos_convert_spaced_integer4`, `os_convert_spaced_integer4`, `xos_convert_fixed_net_station`, `os_convert_fixed_net_station`, `xos_convert_net_station`, `os_convert_net_station`, `xos_convert_fixed_file_size`, `os_convert_fixed_file_size`, `xos_convert_file_size`, `os_convert_file_size`, `xos_null`, `xos_char_to_printer`, `xos_printer_on`, `xos_printer_off`, `xos_split_cursors`, `xos_join_cursors`, `xos_vdu_on`, `xos_bell`, `xos_backspace`, `xos_tab`, `xos_line_feed`, `xos_vertical_tab`, `xos_cls`, `xos_return`, `xos_page_mode_on`, `xos_page_mode_off`, `xos_clg`, `xos_set_text_colour`, `xos_set_gcol`, `xos_set_palette`, `xos_reset_colours`, `xos_vdu_off`, `xos_set_mode`, `xos_misc`, `xos_set_graphics_window`, `xos_plot_vdu`, `xos_reset_windows`, `xos_escape`, `xos_set_text_window`, `xos_set_graphics_origin`, `xos_home_text_cursor`, `xos_set_text_cursor`, `xos_space`, `xos_delete`, `xukvdu23v`, `ukvdu23v`, `xvduxv`, `vduxv`, `xservice_release_fiq`, `service_release_fiq`, `xservice_claim_fiq`, `service_claim_fiq`, `xservice_reset`, `service_reset`, `xservice_key_handler`, `service_key_handler`, `xservice_mode_change`, `service_mode_change`, `xservice_claim_fiq_in_background`, `service_claim_fiq_in_background`, `xservice_memory_moved`, `service_memory_moved`, `xservice_pre_mode_change`, `service_pre_mode_change`, `xservice_mode_extension`, `service_mode_extension`, `xservice_mode_translation`, `service_mode_translation`, `xservice_validate_address`, `service_validate_address`, `xservice_monitor_lead_translation`, `service_monitor_lead_translation`, `xservice_mode_changing`, `service_mode_changing`, `xservice_enumerate_screen_modes`, `service_enumerate_screen_modes`, `xservice_pages_unsafe`, `service_pages_unsafe`, `xservice_pages_safe`, `service_pages_safe`, `xservice_dynamic_area_create`, `service_dynamic_area_create`, `xservice_dynamic_area_remove`, `service_dynamic_area_remove`, `xservice_dynamic_area_renumber`, `service_dynamic_area_renumber`, `xevent_char_input`, `event_char_input`, `xevent_vsync`, `event_vsync`, `xevent_interval_timer`, `event_interval_timer`, `xevent_escape`, `event_escape`, `xevent_mouse_transition`, `event_mouse_transition`, `xevent_key_transition`, `event_key_transition`, `xupcall_move_memory_request`, `upcall_move_memory_request`

## `osbyte.h`

Types: `osbyte_op`, `osbyte_var`

Functions: `xos_byte`, `os_byte`, `xbytev`, `bytev`, `xosbyte`, `xosbyte1`, `osbyte1`, `xosbyte2`, `osbyte2`, `xosbyte_read`, `osbyte_read`, `xosbyte_write`, `osbyte_write`

## `osheap.h`

Types: none

Functions: `xosheap_initialise`, `osheap_initialise`, `xosheap_describe`, `osheap_describe`, `xosheap_alloc`, `osheap_alloc`, `xosheap_free`, `osheap_free`, `xosheap_realloc`, `osheap_realloc`, `xosheap_resize`, `osheap_resize`, `xosheap_read_size`, `osheap_read_size`

## `osmodule.h`

Types: `osmodule_section_no`, `osmodule_status`

Functions: `xosmodule_run`, `osmodule_run`, `xosmodule_load`, `osmodule_load`, `xosmodule_enter`, `osmodule_enter`, `xosmodule_reinit`, `osmodule_reinit`, `xosmodule_kill`, `osmodule_kill`, `xosmodule_info`, `osmodule_info`, `xosmodule_alloc`, `osmodule_alloc`, `xosmodule_free`, `osmodule_free`, `xosmodule_tidy`, `osmodule_tidy`, `xosmodule_clear`, `osmodule_clear`, `xosmodule_add_area`, `osmodule_add_area`, `xosmodule_copy_area`, `osmodule_copy_area`, `xosmodule_enumerate`, `osmodule_enumerate`, `xosmodule_realloc`, `osmodule_realloc`, `xosmodule_instantiate`, `osmodule_instantiate`, `xosmodule_rename`, `osmodule_rename`, `xosmodule_prefer`, `osmodule_prefer`, `xosmodule_add_podule_area`, `osmodule_add_podule_area`, `xosmodule_lookup`, `osmodule_lookup`, `xosmodule_enumerate_rom`, `osmodule_enumerate_rom`, `xosmodule_enumerate_rom_with_info`, `osmodule_enumerate_rom_with_info`, `xservice_uk_command`, `service_uk_command`, `xservice_error`, `service_error`, `xservice_uk_byte`, `service_uk_byte`, `xservice_uk_word`, `service_uk_word`, `xservice_help`, `service_help`, `xservice_uk_config`, `service_uk_config`, `xservice_uk_status`, `service_uk_status`, `xservice_new_application`, `service_new_application`, `xservice_lookup_file_type`, `service_lookup_file_type`, `xservice_post_init`, `service_post_init`, `xservice_syntax_error`, `service_syntax_error`

## `osreadsysinfo.h`

Types: `osreadsysinfo_flags0`, `osreadsysinfo_flags1`, `osreadsysinfo_flags2`

Functions: `xosreadsysinfo_screen_size`, `osreadsysinfo_screen_size`, `xosreadsysinfo_mode`, `osreadsysinfo_mode`, `xosreadsysinfo_machine_id`, `osreadsysinfo_machine_id`, `xosreadsysinfo_71x_features`, `osreadsysinfo_71x_features`

## `osspriteop.h`

Types: `osspriteop_trans_tab`, `osspriteop_trans_tab_base`, `osspriteop_area`, `osspriteop_header`, `osspriteop_id`, `osspriteop_save_area`, `osspriteop_save_area_base`, `osspriteop_flags`, `osspriteop_mode_word`, `osspriteop_action`, `osspriteop_pointer_flags`, `osspriteop_trfm_flags`

Functions: `xosspriteop_screen_save`, `osspriteop_screen_save`, `xosspriteop_screen_load`, `osspriteop_screen_load`, `xosspriteop_read_area_cb`, `osspriteop_read_area_cb`, `xosspriteop_clear_sprites`, `osspriteop_clear_sprites`, `xosspriteop_load_sprite_file`, `osspriteop_load_sprite_file`, `xosspriteop_merge_sprite_file`, `osspriteop_merge_sprite_file`, `xosspriteop_save_sprite_file`, `osspriteop_save_sprite_file`, `xosspriteop_return_name`, `osspriteop_return_name`, `xosspriteop_get_sprite`, `osspriteop_get_sprite`, `xosspriteop_create_sprite`, `osspriteop_create_sprite`, `xosspriteop_get_sprite_user_coords`, `osspriteop_get_sprite_user_coords`, `xosspriteop_verify_area`, `osspriteop_verify_area`, `xosspriteop_select_sprite`, `osspriteop_select_sprite`, `xosspriteop_delete_sprite`, `osspriteop_delete_sprite`, `xosspriteop_rename_sprite`, `osspriteop_rename_sprite`, `xosspriteop_copy_sprite`, `osspriteop_copy_sprite`, `xosspriteop_put_sprite`, `osspriteop_put_sprite`, `xosspriteop_create_mask`, `osspriteop_create_mask`, `xosspriteop_remove_mask`, `osspriteop_remove_mask`, `xosspriteop_insert_row`, `osspriteop_insert_row`, `xosspriteop_delete_row`, `osspriteop_delete_row`, `xosspriteop_flip_about_xaxis`, `osspriteop_flip_about_xaxis`, `xosspriteop_put_sprite_user_coords`, `osspriteop_put_sprite_user_coords`, `xosspriteop_append_sprite`, `osspriteop_append_sprite`, `xosspriteop_set_pointer_shape`, `osspriteop_set_pointer_shape`, `xosspriteop_read_palette_size`, `osspriteop_read_palette_size`, `xosspriteop_remove_palette`, `osspriteop_remove_palette`, `xosspriteop_create_palette`, `osspriteop_create_palette`, `xosspriteop_create_true_palette`, `osspriteop_create_true_palette`, `xosspriteop_read_sprite_size`, `osspriteop_read_sprite_size`, `xosspriteop_read_pixel_colour`, `osspriteop_read_pixel_colour`, `xosspriteop_write_pixel_colour`, `osspriteop_write_pixel_colour`, `xosspriteop_read_pixel_mask`, `osspriteop_read_pixel_mask`, `xosspriteop_write_pixel_mask`, `osspriteop_write_pixel_mask`, `xosspriteop_insert_column`, `osspriteop_insert_column`, `xosspriteop_delete_column`, `osspriteop_delete_column`, `xosspriteop_flip_about_yaxis`, `osspriteop_flip_about_yaxis`, `xosspriteop_plot_mask`, `osspriteop_plot_mask`, `xosspriteop_plot_mask_user_coords`, `osspriteop_plot_mask_user_coords`, `xosspriteop_plot_mask_scaled`, `osspriteop_plot_mask_scaled`, `xosspriteop_paint_char_scaled`, `osspriteop_paint_char_scaled`, `xosspriteop_put_sprite_scaled`, `osspriteop_put_sprite_scaled`, `xosspriteop_put_sprite_scaled_colour_map`, `osspriteop_put_sprite_scaled_colour_map`, `xosspriteop_put_sprite_grey_scaled`, `osspriteop_put_sprite_grey_scaled`, `xosspriteop_remove_left_hand_wastage`, `osspriteop_remove_left_hand_wastage`, `xosspriteop_plot_mask_trfm`, `osspriteop_plot_mask_trfm`, `xosspriteop_put_sprite_trfm`, `osspriteop_put_sprite_trfm`, `xosspriteop_put_sprite_trfm_colour_map`, `osspriteop_put_sprite_trfm_colour_map`, `xosspriteop_insert_delete_rows`, `osspriteop_insert_delete_rows`, `xosspriteop_insert_delete_columns`, `osspriteop_insert_delete_columns`, `xosspriteop_switch_output_to_sprite`, `osspriteop_switch_output_to_sprite`, `xosspriteop_switch_output_to_mask`, `osspriteop_switch_output_to_mask`, `xosspriteop_read_save_area_size`, `osspriteop_read_save_area_size`, `xosspriteop_unswitch_output`, `xservice_switching_output_to_sprite`, `service_switching_output_to_sprite`

## `osword.h`

Types: `osword_line_block`, `osword_timer_block`, `osword_gcol_block`, `osword_char_definition_block`, `osword_palette_block`, `osword_cursor_position_block`, `oswordreadclock_local_string_block`, `oswordreadclock_local_bcd_block`, `oswordreadclock_convert_bcd_to_string_block`, `oswordreadclock_utc_block`, `oswordwriteclock_block`, `oswordwriteclock_block_base`, `oswordpointer_define_block`, `oswordpointer_bbox_block`, `oswordpointer_step_block`, `oswordpointer_position_block`, `osword_screen_base_block`, `osword_block`, `oswordreadclock_op`, `oswordwriteclock_op`, `oswordpointer_op`

Functions: `xosword_read_line`, `osword_read_line`, `xosword_read_system_clock`, `osword_read_system_clock`, `xosword_write_system_clock`, `osword_write_system_clock`, `xosword_read_interval_timer`, `osword_read_interval_timer`, `xosword_write_interval_timer`, `osword_write_interval_timer`, `xosword_read_gcol`, `osword_read_gcol`, `xosword_read_char_definition`, `osword_read_char_definition`, `xosword_read_palette`, `osword_read_palette`, `xosword_write_palette`, `osword_write_palette`, `xosword_read_cursor_position`, `osword_read_cursor_position`, `xoswordreadclock_local_string`, `oswordreadclock_local_string`, `xoswordreadclock_local_bcd`, `oswordreadclock_local_bcd`, `xoswordreadclock_convert_bcd_to_string`, `oswordreadclock_convert_bcd_to_string`, `xoswordreadclock_utc`, `oswordreadclock_utc`, `xoswordwriteclock_time_local_string`, `oswordwriteclock_time_local_string`, `xoswordwriteclock_date_local_string`, `oswordwriteclock_date_local_string`, `xoswordwriteclock_date_and_time_local_string`, `oswordwriteclock_date_and_time_local_string`, `xoswordpointer_define`, `oswordpointer_define`, `xoswordpointer_set_bbox`, `oswordpointer_set_bbox`, `xoswordpointer_step`, `oswordpointer_step`, `xoswordpointer_set_position`, `oswordpointer_set_position`, `xoswordpointer_read_position`, `oswordpointer_read_position`, `xoswordpointer_set_unlinked_position`, `oswordpointer_set_unlinked_position`, `xoswordpointer_read_unlinked_position`, `oswordpointer_read_unlinked_position`, `xosword_write_screen_base`, `osword_write_screen_base`

## `podule.h`

Types: `podule_header`, `podule_section`

Functions: `xpodule_read_id`, `podule_read_id`, `xpodule_read_header`, `podule_read_header`, `xpodule_enumerate_chunks`, `podule_enumerate_chunks`, `xpodule_read_chunk`, `podule_read_chunk`, `xpodule_read_bytes`, `xpodule_write_bytes`, `xpodule_call_loader`, `podule_call_loader`, `xpodule_raw_read`, `xpodule_raw_write`, `xpodule_hardware_address`, `podule_hardware_address`, `xpodule_enumerate_chunks_with_info`, `podule_enumerate_chunks_with_info`, `xpodule_hardware_addresses`, `podule_hardware_addresses`, `xpodule_return_number`, `podule_return_number`, `xpodule_read_info`, `podule_read_info`, `xpodule_set_speed`, `podule_set_speed`, `xservice_pre_reset`, `service_pre_reset`, `xservice_adfs_podule`, `service_adfs_podule`, `xservice_adfs_podule_ide`, `service_adfs_podule_ide`, `xservice_adfs_podule_ide_dying`, `service_adfs_podule_ide_dying`

## `portable.h`

Types: `portable_processor_speed`, `portable_control_flags`, `portable_bmu_variable`, `portable_bmu_flags`, `portable_bmu_command`, `portable_features`, `portable_restart_type`, `portable_status_flags`, `portable_state`

Functions: `xportable_speed`, `portable_speed`, `xportable_control`, `portable_control`, `xportable_read_bmu_variable`, `portable_read_bmu_variable`, `xportable_write_bmu_variable`, `xportable_read_features`, `portable_read_features`, `xportable_idle`, `xportable_stop`, `xportable_status`, `xservice_portable`, `service_portable`

## `screenblanker.h`

Types: none

Functions: `xservice_screen_blanked`, `service_screen_blanked`, `xservice_screen_restored`, `service_screen_restored`

## `screenmodes.h`

Types: none

Functions: `xscreenmodesreadinfo_monitor_title`, `screenmodesreadinfo_monitor_title`

## `serviceinternational.h`

Types: none

Functions: `xserviceinternational_country_name_to_country_number`, `serviceinternational_country_name_to_country_number`, `xserviceinternational_alphabet_name_to_alphabet_number`, `serviceinternational_alphabet_name_to_alphabet_number`, `xserviceinternational_country_number_to_country_name`, `serviceinternational_country_number_to_country_name`, `xserviceinternational_alphabet_number_to_alphabet_name`, `serviceinternational_alphabet_number_to_alphabet_name`, `xserviceinternational_country_number_to_alphabet_number`, `serviceinternational_country_number_to_alphabet_number`, `xserviceinternational_define_chars`, `serviceinternational_define_chars`, `xserviceinternational_new_keyboard`, `serviceinternational_new_keyboard`

## `sharedclibrary.h`

Types: `sharedclibrary_stub`, `sharedclibrary_stub_list`, `sharedclibrary_stub_list_base`

Functions: `xsharedclibrary_lib_init_apcs_r`, `sharedclibrary_lib_init_apcs_r`, `xsharedclibrary_lib_init_module`, `sharedclibrary_lib_init_module`

## `sound.h`

Types: `sound_log_table`, `sound_log_scale_table`, `sound_channel_handler`, `sound_sccb`, `sound_scheduler`, `sound_voice_generator`, `sound_state`, `sound_configuration`, `sound_linear_handler_flags`

Functions: `xsound_configure`, `sound_configure`, `xsound_enable`, `xsound_stereo`, `sound_stereo`, `xsound_speaker`, `xsoundmode_read_configuration`, `soundmode_read_configuration`, `xsoundmode_set_oversampling`, `soundmode_set_oversampling`, `xsound_linear_handler`, `sound_linear_handler`, `xsoundsamplerate_read_count`, `soundsamplerate_read_count`, `xsoundsamplerate_read_current`, `soundsamplerate_read_current`, `xsoundsamplerate_lookup`, `soundsamplerate_lookup`, `xsoundsamplerate_select`, `soundsamplerate_select`, `xsound_volume`, `xsound_sound_log`, `xsound_log_scale`, `xsound_install_voice`, `sound_install_voice`, `xsoundinstallvoice_read_name`, `soundinstallvoice_read_name`, `xsoundinstallvoice_add_named_voice`, `soundinstallvoice_add_named_voice`, `xsoundinstallvoice_read_local_name`, `soundinstallvoice_read_local_name`, `xsoundinstallvoice_change_local_name`, `soundinstallvoice_change_local_name`, `xsound_remove_voice`, `sound_remove_voice`, `xsound_attach_voice`, `sound_attach_voice`, `xsound_control_packed`, `xsound_tuning`, `xsound_pitch`, `xsound_control`, `xsound_attach_named_voice`, `xsound_read_control_block`, `sound_read_control_block`, `xsound_write_control_block`, `sound_write_control_block`, `xsound_qinit`, `xsound_qschedule`, `xsound_qremove`, `xsound_qfree`, `xsound_qtempo`, `xsound_qbeat`, `xservice_sound`, `service_sound`, `xevent_start_of_bar`, `event_start_of_bar`

## `squash.h`

Types: `squash_file`, `squash_file_base`, `squash_input_status`, `squash_output_status`

Functions: `xsquash_compress_return_sizes`, `squash_compress_return_sizes`, `xsquash_compress`, `squash_compress`, `xsquash_decompress_return_sizes`, `squash_decompress_return_sizes`, `xsquash_decompress`, `squash_decompress`

## `territory.h`

Types: `territory_data`, `territory_ordinals`, `territory_property_table`, `territory_calendar`, `territory_t`, `territory_collate_flags`, `territory_time_string_flags`, `territory_write_flags`, `territory_character_property`, `territory_symbol_no`, `territory_symbol_currency_no`

Functions: `xterritory_number`, `xterritory_register`, `xterritory_deregister`, `xterritory_number_to_name`, `xterritory_exists`, `territory_exists`, `xterritory_alphabet_number_to_name`, `xterritory_select_alphabet`, `xterritory_set_time`, `xterritory_read_current_time_zone`, `territory_read_current_time_zone`, `xterritory_convert_time_to_utc_ordinals`, `territory_convert_time_to_utc_ordinals`, `xterritory_read_time_zones`, `territory_read_time_zones`, `xterritory_convert_date_and_time`, `territory_convert_date_and_time`, `xterritory_convert_standard_date_and_time`, `territory_convert_standard_date_and_time`, `xterritory_convert_standard_date`, `territory_convert_standard_date`, `xterritory_convert_standard_time`, `territory_convert_standard_time`, `xterritory_convert_time_to_ordinals`, `xterritory_convert_time_string_to_ordinals`, `xterritory_convert_ordinals_to_time`, `xterritory_alphabet`, `xterritory_alphabet_identifier`, `xterritory_select_keyboard_handler`, `xterritory_write_direction`, `xterritory_character_property_table`, `xterritory_lower_case_table`, `xterritory_upper_case_table`, `xterritory_control_table`, `xterritory_plain_table`, `xterritory_value_table`, `xterritory_representation_table`, `xterritory_collate`, `xterritory_read_boolean_symbols`, `xterritory_read_integer_symbols`, `xterritory_read_string_symbols`, `xterritory_read_calendar_information`, `xterritory_name_to_number`, `xterritory_transform_string`, `xservice_territory_manager_loaded`, `service_territory_manager_loaded`, `xservice_territory_started`, `service_territory_started`

## `types.h`

Types: `bytes`, `bool`, `byte`

Functions: none

