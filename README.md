# Orange Crab DRC

Just learing (again) to do kicad plugins. Finding documentation remains hard but with some tricks nice results can be achieved.

In this case I was able to get some stats on the open source https://github.com/gregdavill/OrangeCrab while learning about ddr3 layout

Results on orangecrab_r0.2

```
Control signals
     cat |        net name | length (mm)
       a |          RAM_A0 | 15.062468
       a |          RAM_A1 | 15.065950
       a |          RAM_A2 | 15.075066
       a |          RAM_A3 | 14.989037
       a |          RAM_A4 | 15.000071
       a |          RAM_A5 | 15.101829
       a |          RAM_A6 | 14.999521
       a |          RAM_A7 | 15.000011
       a |          RAM_A8 | 15.015709
       a |          RAM_A9 | 15.088635
       a |         RAM_A10 | 15.010265
       a |         RAM_A11 | 15.002059
       a |         RAM_A12 | 15.000049
      ba |         RAM_BA0 | 15.082576
      ba |         RAM_BA1 | 14.999790
      ba |         RAM_BA2 | 15.003096
   ras_n |        RAM_RAS# | 15.019889
   cas_n |        RAM_CAS# | 15.002716
    we_n |         RAM_WE# | 15.089160
    cs_n |         RAM_CS# | 15.045750
   clk_p |         RAM_CK+ | 16.120576
   clk_n |         RAM_CK- | 16.929909
     cke |         RAM_CKE | 15.020425
     odt |         RAM_ODT | 15.002260
 reset_n |      RAM_RESET# | 28.993378
min: 14.989037, max: 28.993378, diff 14.004342
Data path
       net name | length (mm)
      dm |         RAM_LDM | 15.845067
      dm |         RAM_UDM | 15.449239
      dq |          RAM_D0 | 15.379386
      dq |          RAM_D1 | 15.356792
      dq |          RAM_D2 | 15.350022
      dq |          RAM_D3 | 15.350081
      dq |          RAM_D4 | 15.320676
      dq |          RAM_D5 | 15.850099
      dq |          RAM_D6 | 15.850024
      dq |          RAM_D7 | 15.850063
      dq |          RAM_D8 | 15.914202
      dq |          RAM_D9 | 15.843592
      dq |         RAM_D10 | 15.895227
      dq |         RAM_D11 | 15.844602
      dq |         RAM_D12 | 15.838853
      dq |         RAM_D13 | 15.845041
      dq |         RAM_D14 | 15.850062
      dq |         RAM_D15 | 15.845015
   dqs_p |       RAM_UDQS+ | 15.395239
   dqs_p |       RAM_UDQS- | 15.350055
   dqs_n |       RAM_LDQS+ | 15.850063
   dqs_n |       RAM_LDQS- | 15.850019
min: 15.320676, max: 15.914202, diff 0.593526
```
