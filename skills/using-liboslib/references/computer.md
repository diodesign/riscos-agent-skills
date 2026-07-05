# Computer OSLib components

File system, filing system, network, serial, device, and machine-level Computer interfaces.

Public C headers are under `.../OSLib/Computer/h`. The matching `hdr/` directory contains the parallel assembler/DefMod interface names for the same logical components.

## `adfs.h`

Types: `adfs_controller`

Functions: `xadfsdiscop_verify`, `adfsdiscop_verify`, `xadfsdiscop_read_sectors`, `adfsdiscop_read_sectors`, `xadfsdiscop_write_sectors`, `adfsdiscop_write_sectors`, `xadfsdiscop_read_track`, `adfsdiscop_read_track`, `xadfsdiscop_read_id`, `adfsdiscop_read_id`, `xadfsdiscop_write_track`, `adfsdiscop_write_track`, `xadfsdiscop_format_track`, `adfsdiscop_format_track`, `xadfsdiscop_seek`, `adfsdiscop_seek`, `xadfsdiscop_restore`, `adfsdiscop_restore`, `xadfsdiscop_step_in`, `adfsdiscop_step_in`, `xadfsdiscop_step_out`, `adfsdiscop_step_out`, `xadfsdiscop_read_sectors_via_cache`, `adfsdiscop_read_sectors_via_cache`, `xadfsdiscop_specify`, `adfsdiscop_specify`, `xadfs_hdc`, `adfs_hdc`, `xadfs_drives`, `adfs_drives`, `xadfs_free_space`, `adfs_free_space`, `xadfs_retries`, `adfs_retries`, `xadfs_describe_disc`, `xadfs_vet_format`, `xadfs_controller_type`, `xadfspowercontrol_read_spin`, `adfspowercontrol_read_spin`, `xadfspowercontrol_set_autospindown`, `adfspowercontrol_set_autospindown`, `xadfspowercontrol_set_spin`, `adfspowercontrol_set_spin`, `xadfs_set_ide_controller`, `adfs_set_ide_controller`, `xadfs_ide_user_op`, `adfs_ide_user_op`, `xadfsmiscop_mount`, `adfsmiscop_mount`, `xadfsmiscop_poll_changed`, `adfsmiscop_poll_changed`, `xadfsmiscop_lock_drive`, `adfsmiscop_lock_drive`, `xadfsmiscop_unlock_drive`, `adfsmiscop_unlock_drive`, `xadfsmiscop_poll_period`, `adfsmiscop_poll_period`, `xadfsmiscop_eject_disc`, `adfsmiscop_eject_disc`, `xadfsmiscop_read_info`, `adfsmiscop_read_info`, `xadfs_lock_ide`, `xservice_identify_format`, `service_identify_format`, `xservice_display_format_help`, `service_display_format_help`

## `cd.h`

Types: `cd_control_block`, `cd_version_block`, `cd_parameter_block`, `cd_enquire_all_tracks_block`, `cd_enquire_one_track_block`, `cd_sub_channel_block`, `cd_disc_used_block`, `cd_inquiry_block`, `cd_register_block`, `cd_volume_block`, `cd_address`, `cd_address_mode`, `cd_audio_flags`, `cd_status`, `cd_readiness`, `cd_multiplier`, `cd_data_mode`, `cd_speed`, `cd_play_to_what`, `cd_audio`, `cd_error_response_level`, `cd_flags`, `cd_register_flags`, `cd_drive_type`, `cd_audio_completion`

Functions: `xcd_version`, `xcd_read_data`, `cd_read_data`, `xcd_seek_to`, `cd_seek_to`, `xcd_drive_status`, `cd_drive_status`, `xcd_drive_ready`, `cd_drive_ready`, `xcd_get_parameters`, `cd_get_parameters`, `xcd_set_parameters`, `cd_set_parameters`, `xcd_open_drawer`, `cd_open_drawer`, `xcd_eject_button`, `cd_eject_button`, `xcd_enquire_address`, `cd_enquire_address`, `xcd_enquire_data_mode`, `cd_enquire_data_mode`, `xcd_play_audio`, `cd_play_audio`, `xcd_play_track`, `cd_play_track`, `xcd_audio_pause`, `cd_audio_pause`, `xcd_enquire_all_tracks`, `cd_enquire_all_tracks`, `xcd_enquire_one_track`, `cd_enquire_one_track`, `xcd_read_sub_channel`, `cd_read_sub_channel`, `xcd_check_drive`, `cd_check_drive`, `xcd_disc_changed`, `cd_disc_changed`, `xcd_stop_disc`, `cd_stop_disc`, `xcd_disc_used`, `cd_disc_used`, `xcd_audio_status`, `cd_audio_status`, `xcd_inquiry`, `cd_inquiry`, `xcd_disc_has_changed`, `cd_disc_has_changed`, `xcd_control`, `cd_control`, `xcd_supported`, `cd_supported`, `xcd_prefetch`, `cd_prefetch`, `xcd_reset`, `cd_reset`, `xcd_close_drawer`, `cd_close_drawer`, `xcd_is_drawer_locked`, `cd_is_drawer_locked`, `xcd_audio_control`, `cd_audio_control`, `xcd_last_error`, `xcd_audio_level`, `cd_audio_level`, `xcd_register`, `xcd_unregister`, `xcd_byte_copy`, `cd_byte_copy`, `xcd_identify`, `cd_identify`, `xcd_convert_to_lba`, `cd_convert_to_lba`, `xcd_convert_to_msf`, `cd_convert_to_msf`, `xcd_read_audio`, `cd_read_audio`, `xcd_read_user_data`, `cd_read_user_data`, `xcd_seek_user_data`, `cd_seek_user_data`, `xcdgetaudioparms_volume_block`, `cdgetaudioparms_volume_block`

## `cdfs.h`

Types: `cdfs_truncation_type`

Functions: `xcdfs_convert_drive_to_device`, `cdfs_convert_drive_to_device`, `xcdfs_set_buffer_size`, `xcdfs_get_buffer_size`, `xcdfs_set_number_of_drives`, `xcdfs_get_number_of_drives`, `xcdfs_give_file_type`, `cdfs_give_file_type`, `xcdfs_describe_disc`, `xcdfs_where_is_file`, `cdfs_where_is_file`, `xcdfstruncation_read`, `cdfstruncation_read`, `xcdfstruncation_write`, `cdfstruncation_write`

## `devicefs.h`

Types: `devicefs_d`, `devicefs_s`, `devicefs_h`, `devicefs_device`, `devicefs_device_list`, `devicefs_device_list_base`, `devicefs_flags`, `devicefs_register_flags`, `devicefs_initialise_flags`

Functions: `xdevicefs_register`, `devicefs_register`, `xdevicefs_deregister`, `xdevicefs_register_objects`, `xdevicefs_deregister_objects`, `xdevicefscalldevice_initialise`, `devicefscalldevice_initialise`, `xdevicefscalldevice_terminate`, `devicefscalldevice_terminate`, `xdevicefscalldevice_tx_wake_up`, `devicefscalldevice_tx_wake_up`, `xdevicefscalldevice_rx_wake_up`, `devicefscalldevice_rx_wake_up`, `xdevicefscalldevice_rx_sleep`, `devicefscalldevice_rx_sleep`, `xdevicefscalldevice_enum_dir`, `devicefscalldevice_enum_dir`, `xdevicefscalldevice_tx_create_buffer`, `devicefscalldevice_tx_create_buffer`, `xdevicefscalldevice_rx_create_buffer`, `devicefscalldevice_rx_create_buffer`, `xdevicefscalldevice_halt`, `devicefscalldevice_halt`, `xdevicefscalldevice_resume`, `devicefscalldevice_resume`, `xdevicefscalldevice_end_of_data`, `devicefscalldevice_end_of_data`, `xdevicefscalldevice_stream_created`, `devicefscalldevice_stream_created`, `xdevicefs_threshold`, `devicefs_threshold`, `xdevicefs_received_char`, `devicefs_received_char`, `xdevicefs_transmit_char`, `devicefs_transmit_char`, `xservice_device_fs_starting`, `service_device_fs_starting`, `xservice_device_fs_dying`, `service_device_fs_dying`, `xservice_device_dead`, `service_device_dead`, `xservice_device_fs_close_request`, `service_device_fs_close_request`, `xupcall_stream_created`, `upcall_stream_created`, `xupcall_stream_closed`, `upcall_stream_closed`, `xevent_device_overrun`, `event_device_overrun`

## `dosfs.h`

Types: `dosfs_format_specifier`

Functions: `xdosfs_disc_format`, `xdosfs_layout_structure`, `xdosfs_layout_structure_given_size`, `dosfs_layout_structure_given_size`

## `econet.h`

Types: `econet_rx_cb`, `econet_tx_cb`, `econet_status`, `econet_immediate_op`, `econet_immediate_os_procedure`, `econet_protection`, `econet_transport_type`, `econet_state`, `econet_action`, `econet_map_flags`

Functions: `xeconet_create_receive`, `econet_create_receive`, `xeconet_examine_receive`, `xeconet_read_receive`, `econet_read_receive`, `xeconet_abandon_receive`, `xeconet_wait_for_reception`, `econet_wait_for_reception`, `xeconet_enumerate_receive`, `xeconet_start_transmit`, `econet_start_transmit`, `xeconet_poll_transmit`, `xeconet_abandon_transmit`, `xeconet_do_transmit`, `econet_do_transmit`, `xeconet_read_local_station_and_net`, `econet_read_local_station_and_net`, `xeconet_convert_status_to_string`, `econet_convert_status_to_string`, `xeconet_convert_status_to_error`, `econet_convert_status_to_error`, `xeconet_read_protection`, `xeconet_set_protection`, `xeconet_read_station_number`, `econet_read_station_number`, `xeconet_print_banner`, `xeconet_read_transport_type`, `econet_read_transport_type`, `xeconet_release_port`, `xeconet_allocate_port`, `xeconet_de_allocate_port`, `xeconet_claim_port`, `xeconet_start_immediate`, `econet_start_immediate`, `xeconet_do_immediate`, `econet_do_immediate`, `xeconet_abandon_and_read_receive`, `econet_abandon_and_read_receive`, `xeconet_version`, `econet_version`, `xeconet_network_state`, `econet_network_state`, `xeconet_packet_size`, `econet_packet_size`, `xeconet_read_transport_name`, `econet_read_transport_name`, `xeconet_enumerate_map`, `econet_enumerate_map`, `xeconet_enumerate_transmit`, `xeconet_hardware_addresses`, `econet_hardware_addresses`, `xeconetv`, `econetv`, `xservice_reallocate_ports`, `service_reallocate_ports`, `xservice_econet_dying`, `service_econet_dying`, `xservice_protocol_dying`, `service_protocol_dying`, `xservice_find_network_driver`, `service_find_network_driver`, `xservice_network_driver_status`, `service_network_driver_status`, `xevent_econet_user_rpc`, `event_econet_user_rpc`, `xevent_econet_rx`, `event_econet_rx`, `xevent_econet_tx`, `event_econet_tx`, `xevent_econet_os_proc`, `event_econet_os_proc`

## `filecore.h`

Types: `filecore_descriptor`, `filecore_disc`, `filecore_format`, `filecore_track_format`, `filecore_track_format_base`, `filecore_defect_list`, `filecore_defect_list_base`, `filecore_info`, `filecore_disc_address`

Functions: `xfilecorediscop_verify`, `filecorediscop_verify`, `xfilecorediscop_read_sectors`, `filecorediscop_read_sectors`, `xfilecorediscop_write_sectors`, `filecorediscop_write_sectors`, `xfilecorediscop_read_track`, `filecorediscop_read_track`, `xfilecorediscop_read_id`, `filecorediscop_read_id`, `xfilecorediscop_write_track`, `filecorediscop_write_track`, `xfilecorediscop_format_track`, `filecorediscop_format_track`, `xfilecorediscop_seek`, `filecorediscop_seek`, `xfilecorediscop_restore`, `filecorediscop_restore`, `xfilecorediscop_step_in`, `filecorediscop_step_in`, `xfilecorediscop_step_out`, `filecorediscop_step_out`, `xfilecorediscop_read_sectors_via_cache`, `filecorediscop_read_sectors_via_cache`, `xfilecorediscop_specify`, `filecorediscop_specify`, `xfilecore_create`, `filecore_create`, `xfilecore_drives`, `filecore_drives`, `xfilecore_free_space`, `filecore_free_space`, `xfilecore_floppy_structure`, `filecore_floppy_structure`, `xfilecore_describe_disc`, `filecore_describe_disc`, `xfilecore_discard_read_sectors_cache`, `filecore_discard_read_sectors_cache`, `xfilecore_disc_format`, `xfilecore_layout_structure`, `xfilecoremiscop_mount`, `filecoremiscop_mount`, `xfilecoremiscop_poll_changed`, `filecoremiscop_poll_changed`, `xfilecoremiscop_lock_drive`, `filecoremiscop_lock_drive`, `xfilecoremiscop_unlock_drive`, `filecoremiscop_unlock_drive`, `xfilecoremiscop_poll_period`, `filecoremiscop_poll_period`, `xfilecoremiscop_eject_disc`, `filecoremiscop_eject_disc`, `xfilecoremiscop_read_info`, `filecoremiscop_read_info`, `xfilecore_free_space64`, `filecore_free_space64`, `xservice_identify_disc`, `service_identify_disc`

## `filer.h`

Types: `filer_message_open_dir`, `filer_message_open_dir_at`, `filer_message_selection_dir`, `filer_message_add_selection`, `filer_message_action`, `filer_message_control_action`, `filer_message_selection`, `filer_format`

Functions: `xservice_start_filer`, `service_start_filer`, `xservice_started_filer`, `service_started_filer`, `xservice_filer_dying`, `service_filer_dying`, `xservice_enumerate_formats`, `service_enumerate_formats`, `xservice_disc_dismounted`, `service_disc_dismounted`

## `fileraction.h`

Types: `fileraction_flags`

Functions: `xfileraction_send_selected_directory`, `xfileraction_send_selected_file`, `xfileractionsendstartoperation_copy`, `fileractionsendstartoperation_copy`, `xfileractionsendstartoperation_move_local`, `fileractionsendstartoperation_move_local`, `xfileractionsendstartoperation_delete`, `fileractionsendstartoperation_delete`, `xfileractionsendstartoperation_access`, `fileractionsendstartoperation_access`, `xfileractionsendstartoperation_set_type`, `fileractionsendstartoperation_set_type`, `xfileractionsendstartoperation_count`, `fileractionsendstartoperation_count`, `xfileractionsendstartoperation_move`, `fileractionsendstartoperation_move`, `xfileractionsendstartoperation_copy_local`, `fileractionsendstartoperation_copy_local`, `xfileractionsendstartoperation_stamp`, `fileractionsendstartoperation_stamp`, `xfileractionsendstartoperation_find`, `fileractionsendstartoperation_find`

## `fileswitch.h`

Types: `fileswitch_info_words`, `fileswitch_fs_no`, `fileswitch_fs_info`, `fileswitch_fs_extra_info`, `fileswitch_object_type`, `fileswitch_attr`

Functions: `xos_bget`, `os_bget`, `xbgetv`, `bgetv`, `xos_bput`, `xbputv`, `bputv`, `xservice_start_up_fs`, `service_start_up_fs`, `xservice_fs_redeclare`, `service_fs_redeclare`, `xservice_close_file`, `service_close_file`

## `free.h`

Types: none

Functions: `xfree_register`, `xfree_de_register`

## `freeway.h`

Types: `freeway_object_type`, `freeway_interest_flags`, `freeway_object_flags`, `freeway_read_flags`, `freeway_enumerate_flags`, `freeway_starting_flags`, `freeway_terminating_flags`, `freeway_upcall_reason`

Functions: `xfreeway_register`, `xfreeway_write`, `freeway_write`, `xfreeway_read`, `freeway_read`, `xfreeway_enumerate`, `freeway_enumerate`, `xservice_freeway_starting`, `service_freeway_starting`, `xservice_freeway_terminating`, `service_freeway_terminating`, `xupcall_freeway`, `upcall_freeway`

## `fslock.h`

Types: `fslock_lock_status`

Functions: `xfslock_version`, `fslock_version`, `xfslock_status`, `fslock_status`, `xfslock_change_status`

## `joystick.h`

Types: `joystick_state`, `joystick_half_word_state`

Functions: `xjoystick_read`, `xjoystick_read_half_word`, `joystick_read_half_word`, `xjoystick_calibrate_top_right`, `xjoystick_calibrate_bottom_left`

## `netfs.h`

Types: `netfs_cli_request`, `netfs_save_request`, `netfs_save_reply`, `netfs_save_final_reply`, `netfs_load_request`, `netfs_load_reply`, `netfs_ex_request`, `netfs_cat_request`, `netfs_cat_reply`, `netfs_open_request`, `netfs_open_reply`, `netfs_close_request`, `netfs_bget_request`, `netfs_bget_reply`, `netfs_bput_request`, `netfs_gbpb_request`, `netfs_gbpb_reply`, `netfs_read_args_request`, `netfs_read_args_reply`, `netfs_set_args_request`, `netfs_read_disc_info_request`, `netfs_disc_info`, `netfs_read_disc_info_reply`, `netfs_read_disc_info_reply_base`, `netfs_read_logon_info_request`, `netfs_logon_info`, `netfs_read_logon_info_reply`, `netfs_read_logon_info_reply_base`, `netfs_read_date_and_time_reply`, `netfs_read_eof_status_request`, `netfs_read_eof_status_reply`, `netfs_read_object_request`, `netfs_delete_object_request`, `netfs_delete_object_reply`, `netfs_read_env_reply`, `netfs_opt_request`, `netfs_read_user_info_request`, `netfs_read_user_info_reply`, `netfs_read_version_reply`, `netfs_read_free_request`, `netfs_read_free_reply`, `netfs_create_dir_request`, `netfs_set_date_and_time_request`, `netfs_create_request`, `netfs_create_reply`, `netfs_read_user_free_request`, `netfs_read_user_free_reply`, `netfs_set_user_free_request`, `netfs_read_user_name_reply`, `netfs_logon_info_extended`, `netfs_read_logon_info_extended_request`, `netfs_read_logon_info_extended_reply`, `netfs_read_logon_info_extended_reply_base`, `netfs_read_user_info_extended_request`, `netfs_read_user_info_extended_reply`, `netfs_cli_info_reply`, `netfs_clii_am_reply`, `netfs_clis_disc_reply`, `netfs_cli_dir_reply`, `netfs_cli_unknown_reply`, `netfs_cli_lib_reply`, `netfs_ex_reply`, `netfs_ex_text_reply`, `netfs_ex_title_reply`, `netfs_ex_title_text_reply`, `netfs_read_object_stamp_reply`, `netfs_read_object_load_and_exec_addr_reply`, `netfs_read_object_size_reply`, `netfs_read_object_attr_reply`, `netfs_read_object_all_info_reply`, `netfs_read_object_attr_and_cycle_no_reply`, `netfs_read_object_sin_reply`, `netfs_set_object_load_exec_and_attr_request`, `netfs_set_object_load_addr_request`, `netfs_set_object_exec_addr_request`, `netfs_set_object_attr_request`, `netfs_set_object_stamp_request`, `netfs_manager_op_read_password_count_request`, `netfs_manager_op_read_password_count_reply`, `netfs_manager_op_read_password_request`, `netfs_manager_op_read_password_reply`, `netfs_manager_op_write_password_request`, `netfs_manager_op_add_user_request`, `netfs_manager_op_remove_user_request`, `netfs_manager_op_set_privilege_request`, `netfs_manager_op_logoff_user_request`, `netfs_cli`, `netfs_save`, `netfs_load`, `netfs_ex`, `netfs_cat`, `netfs_open`, `netfs_close`, `netfs_bget`, `netfs_bput`, `netfs_gbpb`, `netfs_read_args`, `netfs_set_args`, `netfs_read_disc_info`, `netfs_read_logon_info`, `netfs_read_date_and_time`, `netfs_read_eof_status`, `netfs_read_object`, `netfs_set_object`, `netfs_delete_object`, `netfs_read_env`, `netfs_opt`, `netfs_read_user_info`, `netfs_read_version`, `netfs_read_free`, `netfs_create_dir`, `netfs_set_date_and_time`, `netfs_create`, `netfs_read_user_free`, `netfs_set_user_free`, `netfs_read_user_name`, `netfs_read_logon_info_extended`, `netfs_read_user_info_extended`, `netfs_manager_op_read_password_count`, `netfs_manager_op_read_password`, `netfs_manager_op_write_password`, `netfs_manager_op_add_user`, `netfs_manager_op_remove_user`, `netfs_manager_op_set_privilege`, `netfs_manager_op_logoff_user`, `netfs_op`, `netfs_file_server`, `netfs_file_server_context`, `netfs_fs_op`, `netfs_fs_op_ex_type`, `netfs_fs_op_args_type`, `netfs_fs_op_read_object_type`, `netfs_fs_op_set_object_type`, `netfs_fs_op_manager_op_type`

Functions: `xnetfs_read_fs_number`, `netfs_read_fs_number`, `xnetfs_set_fs_number`, `xnetfs_read_fs_name`, `netfs_read_fs_name`, `xnetfs_set_fs_name`, `xnetfs_read_fs_timeouts`, `netfs_read_fs_timeouts`, `xnetfs_set_fs_timeouts`, `netfs_set_fs_timeouts`, `xnetfs_do_fs_op`, `netfs_do_fs_op`, `xnetfs_enumerate_fs_list`, `netfs_enumerate_fs_list`, `xnetfs_enumerate_fs`, `netfs_enumerate_fs`, `xnetfs_convert_date`, `xnetfs_do_fs_op_to_given_fs`, `netfs_do_fs_op_to_given_fs`, `xnetfs_update_fs_list`, `xnetfs_enumerate_fs_contexts`, `netfs_enumerate_fs_contexts`, `xnetfs_read_user_id`, `netfs_read_user_id`, `xnetfs_get_object_uid`, `netfs_get_object_uid`, `xnetfs_enable_cache`, `xservice_net_fs`, `service_net_fs`, `xservice_net_fs_dying`, `service_net_fs_dying`

## `netprint.h`

Types: `netprint_brief_entry`, `netprint_name_entry`, `netprint_full_entry`, `netprint_status`

Functions: `xnetprint_read_ps_number`, `netprint_read_ps_number`, `xnetprint_set_ps_number`, `xnetprint_read_ps_name`, `netprint_read_ps_name`, `xnetprint_set_ps_name`, `xnetprint_read_ps_timeouts`, `netprint_read_ps_timeouts`, `xnetprint_set_ps_timeouts`, `netprint_set_ps_timeouts`, `xnetprint_bind_ps_name`, `netprint_bind_ps_name`, `xnetprintlistservers_brief`, `netprintlistservers_brief`, `xnetprintlistservers_name`, `netprintlistservers_name`, `xnetprintlistservers_full`, `netprintlistservers_full`, `xnetprint_convert_status_to_string`, `netprint_convert_status_to_string`

## `nfs.h`

Types: none

Functions: `xnfs_mount`, `xnfs_mount_list`, `nfs_mount_list`, `xnfs_set_user`, `xnfs_dismount`, `xnfs_mount_info`, `nfs_mount_info`, `xnfs_free_space`, `nfs_free_space`, `xservice_nfs`, `service_nfs`

## `osargs.h`

Types: `osargs_stream_status`

Functions: `xosargs_read_ptr`, `osargs_read_ptr`, `xosargs_read_temporary_fs`, `osargs_read_temporary_fs`, `xosargs_set_ptr`, `osargs_set_ptr`, `xosargs_read_ext`, `osargs_read_ext`, `xosargs_set_ext`, `osargs_set_ext`, `xosargs_read_allocation`, `osargs_read_allocation`, `xosargs_read_eof_status`, `osargs_read_eof_status`, `xosargs_set_allocation`, `osargs_set_allocation`, `xosargs_read_path`, `osargs_read_path`, `xosargs_image_stamped`, `osargs_image_stamped`, `xosargs_read_info`, `osargs_read_info`, `xosargs_ensure`, `osargs_ensure`

## `osfile.h`

Types: none

Functions: `xosfile_save_stamped`, `osfile_save_stamped`, `xosfile_write`, `osfile_write`, `xosfile_write_load`, `osfile_write_load`, `xosfile_write_exec`, `osfile_write_exec`, `xosfile_write_attr`, `osfile_write_attr`, `xosfile_stamp`, `osfile_stamp`, `xosfile_set_type`, `osfile_set_type`, `xosfile_delete`, `osfile_delete`, `xosfile_create_stamped`, `osfile_create_stamped`, `xosfile_create_dir`, `osfile_create_dir`, `xosfile_load_stamped`, `osfile_load_stamped`, `xosfile_load_stamped_path`, `osfile_load_stamped_path`, `xosfile_load_stamped_path_var`, `osfile_load_stamped_path_var`, `xosfile_load_stamped_no_path`, `osfile_load_stamped_no_path`, `xosfile_make_error`, `osfile_make_error`, `xosfile_read_stamped`, `osfile_read_stamped`, `xosfile_read_stamped_path`, `osfile_read_stamped_path`, `xosfile_read_stamped_path_var`, `osfile_read_stamped_path_var`, `xosfile_read_stamped_no_path`, `osfile_read_stamped_no_path`, `xosfile_read_block_size`, `osfile_read_block_size`, `xosfile_save`, `osfile_save`, `xosfile_read`, `osfile_read`, `xosfile_read_path`, `osfile_read_path`, `xosfile_read_path_var`, `osfile_read_path_var`, `xosfile_read_no_path`, `osfile_read_no_path`, `xosfile_create`, `osfile_create`, `xosfile_load`, `osfile_load`, `xosfile_load_path`, `osfile_load_path`, `xosfile_load_path_var`, `osfile_load_path_var`, `xosfile_load_no_path`, `osfile_load_no_path`, `xupcallfile_save`, `upcallfile_save`, `xupcallfile_set_args`, `upcallfile_set_args`, `xupcallfile_set_load_addr`, `upcallfile_set_load_addr`, `xupcallfile_set_exec_addr`, `upcallfile_set_exec_addr`, `xupcallfile_set_attr`, `upcallfile_set_attr`, `xupcallfile_delete`, `upcallfile_delete`, `xupcallfile_create`, `upcallfile_create`, `xupcallfile_create_dir`, `upcallfile_create_dir`

## `osfind.h`

Types: `osfind_flags`

Functions: `xosfind_openin`, `osfind_openin`, `xosfind_openout`, `osfind_openout`, `xosfind_openup`, `osfind_openup`, `xosfind_close`, `osfind_close`, `xupcallfind_create_openup`, `upcallfind_create_openup`, `xupcallfind_openup`, `upcallfind_openup`, `xupcallfind_close`, `upcallfind_close`

## `osfscontrol.h`

Types: `osfscontrol_id`, `osfscontrol_fs_info_block`, `osfscontrol_descriptor`, `osfscontrol_copy_flags`, `osfscontrol_wipe_flags`, `osfscontrol_count_flags`, `osfscontrol_object_kind`, `osfscontrol_special_dir`

Functions: `xosfscontrol_dir`, `osfscontrol_dir`, `xosfscontrol_lib`, `osfscontrol_lib`, `xosfscontrol_start_application`, `osfscontrol_start_application`, `xosfscontrol_run`, `osfscontrol_run`, `xosfscontrol_cat`, `osfscontrol_cat`, `xosfscontrol_ex`, `osfscontrol_ex`, `xosfscontrol_lcat`, `osfscontrol_lcat`, `xosfscontrol_lex`, `osfscontrol_lex`, `xosfscontrol_info`, `osfscontrol_info`, `xosfscontrol_opt`, `osfscontrol_opt`, `xosfscontrol_set_temporary_fs`, `osfscontrol_set_temporary_fs`, `xosfscontrol_add_fs`, `osfscontrol_add_fs`, `xosfscontrol_lookup_fs`, `osfscontrol_lookup_fs`, `xosfscontrol_select_fs`, `osfscontrol_select_fs`, `xosfscontrol_boot_from_fs`, `osfscontrol_boot_from_fs`, `xosfscontrol_remove_fs`, `osfscontrol_remove_fs`, `xosfscontrol_add_secondary_fs`, `osfscontrol_add_secondary_fs`, `xosfscontrol_read_file_type`, `osfscontrol_read_file_type`, `xosfscontrol_restore_current`, `osfscontrol_restore_current`, `xosfscontrol_read_module_base`, `osfscontrol_read_module_base`, `xosfscontrol_read_fs_handle`, `osfscontrol_read_fs_handle`, `xosfscontrol_shut`, `osfscontrol_shut`, `xosfscontrol_shutdown`, `osfscontrol_shutdown`, `xosfscontrol_access`, `osfscontrol_access`, `xosfscontrol_rename`, `osfscontrol_rename`, `xosfscontrol_copy`, `osfscontrol_copy`, `xosfscontrol_wipe`, `osfscontrol_wipe`, `xosfscontrol_count`, `osfscontrol_count`, `xosfscontrol_read_secondary_fs`, `osfscontrol_read_secondary_fs`, `xosfscontrol_file_type_from_string`, `osfscontrol_file_type_from_string`, `xosfscontrol_file_info`, `osfscontrol_file_info`, `xosfscontrol_read_fs_name`, `osfscontrol_read_fs_name`, `xosfscontrol_register_image_fs`, `osfscontrol_register_image_fs`, `xosfscontrol_deregister_image_fs`, `osfscontrol_deregister_image_fs`, `xosfscontrol_canonicalise_path`, `osfscontrol_canonicalise_path`, `xosfscontrol_info_to_file_type`, `osfscontrol_info_to_file_type`, `xosfscontrol_urd`, `osfscontrol_urd`, `xosfscontrol_back`, `osfscontrol_back`, `xosfscontrol_defect_list`, `osfscontrol_defect_list`, `xosfscontrol_add_defect`, `osfscontrol_add_defect`, `xosfscontrol_no_dir`, `osfscontrol_no_dir`, `xosfscontrol_no_urd`, `osfscontrol_no_urd`, `xosfscontrol_no_lib`, `osfscontrol_no_lib`, `xosfscontrol_used_space_map`, `osfscontrol_used_space_map`, `xosfscontrol_read_boot_option`, `osfscontrol_read_boot_option`, `xosfscontrol_write_boot_option`, `osfscontrol_write_boot_option`, `xosfscontrol_free_space`, `osfscontrol_free_space`, `xosfscontrol_name_disc`, `osfscontrol_name_disc`, `xosfscontrol_stamp_image`, `osfscontrol_stamp_image`, `xosfscontrol_object_at_offset`, `osfscontrol_object_at_offset`, `xosfscontrol_set_dir`, `osfscontrol_set_dir`, `xosfscontrol_read_dir`, `osfscontrol_read_dir`, `xosfscontrol_free_space64`, `osfscontrol_free_space64`, `xosfscontrol_defect_list64`, `osfscontrol_defect_list64`, `xosfscontrol_add_defect64`, `osfscontrol_add_defect64`, `xupcall_media_not_present`, `upcall_media_not_present`, `xupcall_media_not_known`, `upcall_media_not_known`, `xupcallfscontrol_set_args_size`, `upcallfscontrol_set_args_size`, `xupcallfscontrol_rename`, `upcallfscontrol_rename`, `xupcallfscontrol_set_attr_string`, `upcallfscontrol_set_attr_string`, `xupcall_media_search_end`, `upcall_media_search_end`, `xupcall_new_application`, `upcall_new_application`

## `osgbpb.h`

Types: `osgbpb_name`, `osgbpb_name_base`, `osgbpb_disc_name`, `osgbpb_dir_name`, `osgbpb_name_list`, `osgbpb_name_list_base`, `osgbpb_info`, `osgbpb_info_base`, `osgbpb_system_info`, `osgbpb_system_info_base`, `osgbpb_info_stamped`, `osgbpb_info_stamped_base`, `osgbpb_string_list`, `osgbpb_string_list_base`, `osgbpb_info_list`, `osgbpb_info_list_base`, `osgbpb_system_info_list`, `osgbpb_system_info_list_base`, `osgbpb_info_stamped_list`, `osgbpb_info_stamped_list_base`, `osgbpb_privilege`

Functions: `xosgbpb_write_at`, `osgbpb_write_at`, `xosgbpb_write`, `osgbpb_write`, `xosgbpb_read_at`, `osgbpb_read_at`, `xosgbpb_read`, `osgbpb_read`, `xosgbpb_read_disc_name`, `osgbpb_read_disc_name`, `xosgbpb_read_csd_name`, `osgbpb_read_csd_name`, `xosgbpb_read_lib_name`, `osgbpb_read_lib_name`, `xosgbpb_csd_entries`, `osgbpb_csd_entries`, `xosgbpb_dir_entries`, `osgbpb_dir_entries`, `xosgbpb_dir_entries_info`, `osgbpb_dir_entries_info`, `xosgbpb_dir_entries_system_info`, `osgbpb_dir_entries_system_info`, `xosgbpb_dir_entries_info_stamped`, `osgbpb_dir_entries_info_stamped`

## `osserialop.h`

Types: `osserialop_rs423_status`, `osserialop_format_flags`, `osserialop_baud_rate`

Functions: `xosserialop_status`, `osserialop_status`, `xosserialop_data_format`, `osserialop_data_format`, `xosserialop_break`, `osserialop_break`, `xosserialop_bput`, `osserialop_bput`, `xosserialop_bget`, `osserialop_bget`, `xosserialop_rx_baud_rate`, `osserialop_rx_baud_rate`, `xosserialop_tx_baud_rate`, `osserialop_tx_baud_rate`, `xosserialop_rx_threshold`, `osserialop_rx_threshold`, `xosserialop_enumerate_baud_rates`, `osserialop_enumerate_baud_rates`, `xevent_rs423_error`, `event_rs423_error`

## `parallel.h`

Types: none

Functions: `xparallelop_read`, `parallelop_read`, `xparallelop_write_data`, `parallelop_write_data`, `xparallelop_write_control`, `parallelop_write_control`

## `pipefs.h`

Types: none

Functions: `xupcall_sleep_no_more`, `upcall_sleep_no_more`

## `ramfs.h`

Types: none

Functions: `xramfsdiscop_verify`, `ramfsdiscop_verify`, `xramfsdiscop_read_sectors`, `ramfsdiscop_read_sectors`, `xramfsdiscop_write_sectors`, `ramfsdiscop_write_sectors`, `xramfsdiscop_read_track`, `ramfsdiscop_read_track`, `xramfsdiscop_read_id`, `ramfsdiscop_read_id`, `xramfsdiscop_write_track`, `ramfsdiscop_write_track`, `xramfsdiscop_format_track`, `ramfsdiscop_format_track`, `xramfsdiscop_seek`, `ramfsdiscop_seek`, `xramfsdiscop_restore`, `ramfsdiscop_restore`, `xramfsdiscop_step_in`, `ramfsdiscop_step_in`, `xramfsdiscop_step_out`, `ramfsdiscop_step_out`, `xramfsdiscop_read_sectors_via_cache`, `ramfsdiscop_read_sectors_via_cache`, `xramfsdiscop_specify`, `ramfsdiscop_specify`, `xramfs_drives`, `ramfs_drives`, `xramfs_free_space`, `ramfs_free_space`, `xramfs_describe_disc`

## `resourcefs.h`

Types: `resourcefs_file_header`, `resourcefs_file_header_base`, `resourcefs_file_data`, `resourcefs_file_data_base`, `resourcefs_file`, `resourcefs_file_list`, `resourcefs_file_list_base`

Functions: `xresourcefs_register_files`, `xresourcefs_deregister_files`, `xservice_resource_fs_started`, `service_resource_fs_started`, `xservice_resource_fs_dying`, `service_resource_fs_dying`, `xservice_resource_fs_starting`, `service_resource_fs_starting`

## `scsi.h`

Types: `scsi_device_description`, `scsi_op_block`, `scsi_op_block_base`, `scsi_card_address_list`, `scsi_card_address_list_base`, `scsi_software_features`, `scsi_hardware_features`, `scsi_device_type`, `scsi_device_flags`, `scsi_device_version`, `scsi_error_response_level`, `scsi_queue_behaviour`, `scsi_disconnection`, `scsi_device_status`

Functions: `xscsi_version`, `scsi_version`, `xscsiinitialise_reset_bus`, `scsiinitialise_reset_bus`, `xscsiinitialise_reset_device`, `scsiinitialise_reset_device`, `xscsiinitialise_determine_device`, `scsiinitialise_determine_device`, `xscsiinitialise_enumerate_device`, `scsiinitialise_enumerate_device`, `xscsicontrol_abort_device`, `scsicontrol_abort_device`, `xscsicontrol_abort_op`, `scsicontrol_abort_op`, `xscsicontrol_set_timeout`, `scsicontrol_set_timeout`, `xscsicontrol_set_error_response`, `scsicontrol_set_error_response`, `xscsicontrol_set_queue_behaviour`, `scsicontrol_set_queue_behaviour`, `xscsicontrol_disconnect`, `scsicontrol_disconnect`, `xscsi_op`, `scsi_op`, `xscsistatus_check_device`, `scsistatus_check_device`, `xscsireserve_claim`, `scsireserve_claim`, `xscsireserve_force_claim`, `scsireserve_force_claim`, `xscsireserve_release`, `scsireserve_release`, `xscsi_list`

## `scsifs.h`

Types: `scsifs_drive_status`

Functions: `xscsifsdiscop_verify`, `scsifsdiscop_verify`, `xscsifsdiscop_read_sectors`, `scsifsdiscop_read_sectors`, `xscsifsdiscop_write_sectors`, `scsifsdiscop_write_sectors`, `xscsifsdiscop_read_track`, `scsifsdiscop_read_track`, `xscsifsdiscop_read_id`, `scsifsdiscop_read_id`, `xscsifsdiscop_write_track`, `scsifsdiscop_write_track`, `xscsifsdiscop_format_track`, `scsifsdiscop_format_track`, `xscsifsdiscop_seek`, `scsifsdiscop_seek`, `xscsifsdiscop_restore`, `scsifsdiscop_restore`, `xscsifsdiscop_read_sectors_via_cache`, `scsifsdiscop_read_sectors_via_cache`, `xscsifsdiscop_specify`, `scsifsdiscop_specify`, `xscsifs_drives`, `scsifs_drives`, `xscsifs_free_space`, `scsifs_free_space`, `xscsifs_describe_disc`, `xscsifs_test_ready`, `scsifs_test_ready`

## `sharefs.h`

Types: `sharefs_attr`, `sharefs_share_flags`, `sharefs_stop_flags`, `sharefs_enumerate_flags`, `sharefs_starting_flags`, `sharefs_terminating_flags`

Functions: `xsharefs_create_share`, `xsharefs_stop_share`, `xsharefs_enumerate_shared`, `sharefs_enumerate_shared`, `xservice_share_fs_starting`, `service_share_fs_starting`, `xservice_share_fs_terminating`, `service_share_fs_terminating`

## `socket.h`

Types: `socket_sockaddr_in`, `socket_sockaddr`, `socket_linger`, `socket_timeval`, `socket_ifreq`, `socket_ifconf`, `socket_s`, `socket_iovec`, `socket_msghdr`, `socket_af`, `socket_sock`, `socket_ipproto`, `socket_level`, `socket_so`, `socket_if_flags`, `socket_ioctl_no`, `socket_msg_flags`, `socket_shutdown_type`, `socket_fdset`, `socket_event_type`

Functions: `xsocket_creat`, `xsocket_bind`, `xsocket_listen`, `xsocket_accept`, `xsocket_connect`, `xsocket_recv`, `xsocket_recvfrom`, `socket_recvfrom`, `xsocket_recvmsg`, `xsocket_send`, `xsocket_sendto`, `socket_sendto`, `xsocket_sendmsg`, `xsocket_shutdown`, `xsocket_setsockopt`, `socket_setsockopt`, `xsocket_getsockopt`, `socket_getsockopt`, `xsocket_getpeername`, `xsocket_getsockname`, `xsocket_close`, `xsocket_select`, `socket_select`, `xsocket_ioctl`, `xsocket_read`, `xsocket_write`, `xsocket_stat`, `xsocket_readv`, `xsocket_writev`, `xsocket_gettsize`, `xevent_internet`, `event_internet`

