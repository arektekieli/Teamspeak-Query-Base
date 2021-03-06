from TeamspeakAbstract import TeamspeakAbstract

class TeamspeakClient(TeamspeakAbstract):
    def __init__(self, teamspeak, resultItem):
        self.teamspeak = teamspeak
        self.attributes = ['clid', 'cid', 'client_idle_time', 'client_unique_identifier', 'client_nickname', 'client_version', 'client_platform', 'client_input_muted', 'client_output_muted', 'client_outputonly_muted', 'client_input_hardware', 'client_output_hardware', 'client_default_channel', 'client_meta_data', 'client_is_recording', 'client_version_sign', 'client_security_hash', 'client_login_name', 'client_database_id', 'client_channel_group_id', 'client_servergroups', 'client_created', 'client_lastconnected', 'client_totalconnections', 'client_away', 'client_away_message', 'client_type', 'client_flag_avatar', 'client_talk_power', 'client_talk_request', 'client_talk_request_msg', 'client_description', 'client_is_talker', 'client_month_bytes_uploaded', 'client_month_bytes_downloaded', 'client_total_bytes_uploaded', 'client_total_bytes_downloaded', 'client_is_priority_speaker', 'client_unread_messages', 'client_nickname_phonetic', 'client_needed_serverquery_view_power', 'client_default_token', 'client_icon_id', 'client_is_channel_commander', 'client_country', 'client_channel_group_inherited_channel_id', 'client_badges', 'client_myteamspeak_id', 'client_integrations', 'client_myteamspeak_avatar', 'client_signed_badges', 'client_base64HashClientUID', 'connection_filetransfer_bandwidth_sent', 'connection_filetransfer_bandwidth_received', 'connection_packets_sent_total', 'connection_bytes_sent_total', 'connection_packets_received_total', 'connection_bytes_received_total', 'connection_bandwidth_sent_last_second_total', 'connection_bandwidth_sent_last_minute_total', 'connection_bandwidth_received_last_second_total', 'connection_bandwidth_received_last_minute_total', 'connection_connected_time', 'connection_client_ip', 'client_lastip', 'cldbid', 'name']
        
        for attr in self.attributes:
            setattr(self, attr, None)
        
        self.updateAttributes(resultItem)

    def update(self):
        x = self.teamspeak.clientinfo(self)
        self.updateAttributes(x)
    
    def toList(self):
        return [{attr: getattr(self, attr)} for attr in self.attributes]

    def toDict(self):
        res = {}
        for attr in self.attributes:
            res.update({attr: getattr(self, attr)})
            
        return res
        