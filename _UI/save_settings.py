import json
import os

"""
	Handles the DoA DSP settings
	
	Project: Kraken DoA DSP
	Author : Tamas Peto
"""

root_path          = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
settings_file_path = os.path.join(root_path,"settings.json")

settings_found =False
if os.path.exists(settings_file_path):
    settings_found = True
    with open(settings_file_path, 'r') as myfile:
        settings=json.loads(myfile.read())        

# DAQ Configuration
center_freq    = settings.get("center_freq", 100.0)
uniform_gain   = settings.get("uniform_gain", 1.4)
gain_1         = settings.get("gain_1", 1.4)
gain_2         = settings.get("gain_2", 1.4)
data_interface = settings.get("data_interface", "eth")
default_ip     = settings.get("default_ip", "0.0.0.0")

# PR Paramaters
en_pr               = settings.get("en_pr", 0)
clutter_cancel_algo = settings.get("clutter_cancel_algo", "Wiener MRE")
max_bistatic_range  = settings.get("max_bistatic_range", 128)
max_doppler         = settings.get("max_doppler", 256)
en_pr_persist       = settings.get("en_pr_persist", 1)
pr_persist_decay    = settings.get("pr_persist_decay", 0.99)
pr_dynrange_min     = settings.get("pr_dynrange_min", -20)
pr_dynrange_max     = settings.get("pr_dynrange_max", 100)
#ant_arrangement = settings.get("ant_arrangement", "ULA")
#ant_spacing     = settings.get("ant_spacing", 0.5)
#doa_method      = settings.get("doa_method", "MUSIC")
#en_fbavg        = settings.get("en_fbavg", 0)
#compass_offset  = settings.get("compass_offset", 0)
#doa_fig_type    = settings.get("doa_fig_type", "Linear plot")

# DSP misc
#en_squelch           = settings.get("en_squelch", 0)
#squelch_threshold_dB = settings.get("squelch_threshold_dB", 0.0)

# Web Interface
en_hw_check         = settings.get("en_hw_check", 0)
en_advanced_daq_cfg = settings.get("en_advanced_daq_cfg", 0) 
logging_level       = settings.get("logging_level", 0)
disable_tooltips    = settings.get("disable_tooltips", 0)

# Check and correct if needed
#if not ant_arrangement in ["ULA", "UCA"]:
#    ant_arrangement="ULA"

#doa_method_dict = {"Bartlett":0, "Capon":1, "MEM":2, "MUSIC":3}
#if not doa_method in doa_method_dict:
#    doa_method = "MUSIC"

#doa_fig_type_dict = {"Linear plot":0, "Polar plot":1, "Compass":2}
#if not doa_fig_type in doa_fig_type_dict:
#    doa_gfig_type="Linear plot"

def write(data = None):
    if data is None:
        data = {}

        # DAQ Configuration
        data["center_freq"]    = center_freq    
        data["uniform_gain"]   = uniform_gain
        data["gain_1"]         = gain_1
        data["gain_2"]         = gain_2
        data["data_interface"] = data_interface
        data["default_ip"]     = default_ip

        # DOA Estimation
        data["en_pr"]           = en_pr
        data["clutter_cancel_algo"] = clutter_cancel_algo
        data["max_bistatic_range"] = max_bistatic_range
        data["max_doppler"] = max_doppler
        data["en_pr_persist"] = en_pr_persist
        data["pr_persist_decay"] = pr_persist_decay 
        data["pr_dynrange_min"] = pr_dynrange_min
        data["pr_dynrange_max"] = pr_dynrange_max

        #data["ant_arrangement"] = ant_arrangement
        #data["ant_spacing"]     = ant_spacing
        #data["doa_method"]      = doa_method
        #data["en_fbavg"]        = en_fbavg
        #data["compass_offset"]  = compass_offset
        #data["doa_fig_tpye"]    = doa_fig_type

        # DSP misc        
        #data["en_squelch"]           = en_squelch
        #data["squelch_threshold_dB"] = squelch_threshold_dB

        # Web Interface
        data["en_hw_check"]         = en_hw_check
        data["en_advanced_daq_cfg"] = en_advanced_daq_cfg
        data["logging_level"]       = logging_level
        data["disable_tooltips"]    = disable_tooltips

    with open(settings_file_path, 'w') as outfile:
        json.dump(data, outfile)
