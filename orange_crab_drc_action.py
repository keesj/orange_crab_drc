#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  action_orange_crab_drc
#

import wx
import pcbnew
import os
import logging
import sys

from pad2pad_track_distance import Distance

# https://docs.kicad-pcb.org/doxygen/md_Documentation_development_pcbnew-plugins.html

# Inspired from https://github.com/enjoy-digital/litex/blob/master/litex/boards/platforms/arty.py 

platform = {
        "ddram": {
        "a": [ "RAM_A0", "RAM_A1","RAM_A2","RAM_A3",
            "RAM_A4","RAM_A5","RAM_A6","RAM_A7",
            "RAM_A8","RAM_A9","RAM_A10","RAM_A11",
            "RAM_A12"],
        "ba": ["RAM_BA0","RAM_BA1","RAM_BA2"],
        "ras_n" : ["RAM_RAS#"],
        "cas_n" : ["RAM_CAS#"],
        "we_n": ["RAM_WE#"],
        "cs_n": ["RAM_CS#"],
        "dm" : ["RAM_LDM","RAM_UDM"],
        "dq": [
            "RAM_D0","RAM_D1","RAM_D2","RAM_D3","RAM_D4","RAM_D5","RAM_D6","RAM_D7","RAM_D8","RAM_D9","RAM_D10","RAM_D11","RAM_D12","RAM_D13","RAM_D14","RAM_D15"],
        "dqs_p" : ["RAM_UDQS+","RAM_UDQS-"],# Upper byte data strobe
        "dqs_n" : ["RAM_LDQS+","RAM_LDQS-"],# Lower byte data strobe
        "clk_p" : ["RAM_CK+"],
        "clk_n" : ["RAM_CK-"],
        "cke" : ["RAM_CKE"],
        "odt" : ["RAM_ODT"],
        "reset_n": ["RAM_RESET#"],
        } ,
}

class OrangeCrabDrc(pcbnew.ActionPlugin):
    """
    A script perform some DRC on the Orange Crab
    """

    def defaults(self):
        self.name = "OrangeCrab DRC"
        self.category = "Design rule check"
        self.description = "Perform DRC on the Orange Crab board"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(
                os.path.dirname(__file__), 'orange_crab_drc.png')

    #
    # Calculate the lenght of the net between to chips (modules) on a board
    # given the net name
    def net_length(self,board,source_module, target_module, net):

        source_pad = None
        # not find the pads on the host and ddr chip that are connected to the net
        for pad in source_module.Pads():
            if pad.GetNetname() == net.GetNetname():
                source_pad = pad

        assert(source_pad != None)

        target_pad = None
        for pad in target_module.Pads():
            if pad.GetNetname() == net.GetNetname():
                target_pad = pad
        
        assert(target_pad != None)
        return Distance(board,source_pad,target_pad).get_length()

    def drc(self,board):
        modules = board.GetModules()
        
        # Find the host and ddr chip
        host_chip = board.FindModuleByReference("U3")
        ddr_chip = board.FindModuleByReference("U4")

        nets = board.GetNetInfo().NetsByName()

        # check adddress linnes
        ddram = platform['ddram']

        control_path = [
        "a",
        "ba",
        "ras_n",
        "cas_n",
        "we_n",
        "cs_n",
        "clk_p",
        "clk_n",
        "cke",
        "odt",
        "reset_n"
        ]

        data_path = [
        "dm", 
        "dq",
        "dqs_p",
        "dqs_n",
        ]
       
        print("Control signals")
        sizes = []
        print("%8s | %15s | %s" % ("cat","net name","length (mm)"))
        for line in control_path:
            for net_name in ddram[line]:
                # find the nets we are intersted in
                net = nets[net_name]
                (l,res) = self.net_length(board,host_chip, ddr_chip, net)
                sizes.append(l)
                print("%8s | %15s | %f" % (line,net_name,l))
        print("min: %f, max: %f, diff %f" % (min(sizes),max(sizes),max(sizes)- min(sizes)))

        print("Data path")
        sizes = []
        print("%15s | %s" % ("net name","length (mm)"))
        for line in data_path:
            for net_name in ddram[line]:
                # find the nets we are intersted in
                net = nets[net_name]
                (l,res) = self.net_length(board,host_chip, ddr_chip, net)
                sizes.append(l)
                print("%8s | %15s | %f" % (line,net_name,l))
        print("min: %f, max: %f, diff %f" % (min(sizes),max(sizes),max(sizes)- min(sizes)))
    def Run(self):
        print("WOT")
        # load board
        board = pcbnew.GetBoard()

        # get user units
        if pcbnew.GetUserUnits() == 1:
            user_units = 'mm'
        else:
            user_units = 'in'
        self.drc(board)
        
if __name__ == "__main__":
    ocd = OrangeCrabDrc()
    ocd.drc(pcbnew.LoadBoard("OrangeCrab.kicad_pcb"))
