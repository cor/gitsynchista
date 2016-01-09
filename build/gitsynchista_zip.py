# This is a self-extracting archive. Copy this script into a '.py' file located in the root
# directory of Pythonista and call the script. It will unzip the data and extract all files to an
# immediate sub directory of the root directory.
#
# This file was generated using pyzipista (see https://github.com/marcus67/pyzipista)
#
# Zipped Application:    gitsynchista
# Application Home Page: https://github.com/marcus67/gitsynchista

import zipfile
import base64
import StringIO

zip_string='''
UEsDBBQAAAAIAJYBnUcptW2jmBoAAH9GAAAUAAAAZ2l0c3luY2hpc3RhL0xJQ0VOU0WdXG1z28iR&j6&YkpfLFXR9Np3yWVXV1dFSZTFRKYUkrKjbwHJoYgYBHgYQFpWKv&9_unuAQZ88e7FlY0tEpjp6denX0bWHv75PH6yn4fj4WRwbx_fru5H15b_G46nQ3Pkafz56kqfFrn91LN&rnNnP&7880dj7HWx3ZXpy7qy59cX9OGffu7xV&a2dM5Oi1X1lpTO3hZ1vkwqWqBnR&mi37P&va6q7S8fPqz8ql_ULx&_x9g&4K0k&56luZ1W9H7Vs7fpqlrb26woyp69KnyFFb4M7E_fPn786f3H&&jpo32aDowdvrpyVxBdqbdbV27SqnJLWxV2QQTaJF&aZeqrMp3XlbP07JyI2eDL1Hlji5Wt1vRmli5c7p1dFot643Lan563i3WSv6T5i00rLJ8XlU2yrHhzy745xS7_81i6ZDPPHJ6arV1Y3ttVUdoNHcb6wCD8t3Q_fcmF7Cr5Th__JTu7K_rSrIgby2KDb&yan6cTMV104qpv7dWODpNXZeKJ6Ir2Ygm73JVJZh&rOW1t7vV0dIY0r1y_lK1e6oS4XpG4sJX90Vb4zgSa37_nRzag09f0GDZtjkNb4Fk_KPGKaPS29qRCfXAi9aZLmg2kJdttRhLB5swfFozrKpNplemdjziY82mSfGcLeqe027J4KZONfVsXWLmu1kXpiUsbUg560tReZEoknU_LjdPXTilu53CLgnSI2DffmcDse_fpgPbEwdLcVy5Z9i_sfS5qu0hyPuvOCi3MeSXYkwCLglXr29rl9o34unXJdzCDmRoI6eErEFS6lStLnIYYoPLrQU&NtqT96YAP9SnK&IHqxSJNKiiFWSevIuBIOSJ7EjM6oM_eq_qUL6wJhm2MmPRKW9t0haXtW_rXF71mKzrLwqWvWKQuF1h6SYIpmWEvjuyvMuFF0ln6MXoVz6iidpSRXifds0TjQqjEIrnN3ZvQG&h_KToUlvueF2&NussCa3qsTHz2LJ1ZgVcrt6jEctgPepZK7iJelg6cWkCJvCxPzJinS0O6CpcFZrqcLV03kZVAODTaf5evCkilhN2WfEB5qm9m8k5nF7JonyUVL75wZZXQgemJLX2ZztMsrVJ1Q1hZOGqOSjTmZA8UKfs3xTJdQX2ZFbf0hfs12WwzekifOLqcrxdrmwSWE6&WDlZn6Kcq5ROzy7ArRwvxPjW5gZdU9Y_0I6WlcmIO3ErLBeYrzMhCV&tiZfzunjrTKzs2sF6japF60bcm0jxaZ0Aq0dDh16QS9MwmKANFGrggXlUUhv6VliaIBjbsjmkJ6T3FteqNZFq5rf&Fnn_84FglwbTLdVJLc&7pgvhHdq5qEkWrt3VKTAWPPH_ZuRcyc46CnmO2hsFeLGFa8wNHIRZjvB9TPcg8cQiycAkkxt6T3K0eBavCWOhAovBsjUHhVeEMM9yFyFxDcX1Fr&lGFOJN84LeLxGEdrwln64Ta0gQo9VBiGHiU3bD9PnGYReXeYkF24T8MVGYgz6j3sLHGkTkqsiImLegHKxAIc5jx4JEkuZJ1qM95EiIMcQIiuwbDqVlsawXQgbHEEiXtBMLkGvOIHpIIVrLaDh6Rw9s64oDjKjLLb7Odj3eJHZPIKlaE6KgyE17UbQHLysKIXx6jY1bfF0hzJLewbeyB3kt0iXvv4R3LOXEFL_COiAwknEmwvQmcOIQab5MX9NlDaJsMWdHIps0cIYsPreOdHPB1sZxaN0uQ39TGHJVUu766jRJJ6AuJGZWHub4JlkCy9hF5hKlkFigBxLzmzcQaimqqar1TtEGvDx9DL43zyUM1voBgm0h&8ZyOT4VdELxmlgThkIn6LXuS3XdiLYtBAysCiDAE&jvx_h6Npx8mdrB_MZeP4xvRrPRw3hqbx8m9OPj82j8uWdvRtPZZHT1hK&4wS8PN6Pb0fUAH2DLn&qMoo7BJtVN5jwdRzDNW1F_VzcBlEgy9CYBnxCIt1miygsNaX3QusgQaXyyU_y7ITRKImidyNLUTTAShgYgfRxr9EUGZ49C3xnBa0dc7BkGMA35HCOiM4B6doKkoGd8lHkips07h9XMxlHQsy7lI0ffYA2sS6SmryQ_UjZeRYhvD5wlb7_IgadMC52ctpVnlW2q252V7bYoWScYWfSMEtAkGTgBnH2sPz743yZQL_FIcH6WmMnIUOvkBSw7vyM3SV5hRSzuNS9gQwbyi6wGkMcWRQ3FJ3irX_cmSMaexbufAYYO4dfVTNjfJctl6dhnJt6eUSA5I&UekK9&FbRQKF_Bsk4ZSeeQjCyBQlu0LNqh6nAp&pYhWl35lO2fwimtHlQlgetcmbLOD1ivHjrAHrfsKXzj1cipkk8oNvErJgLuRQ7sveINIVsOCOxT04rDoz1QNBN2Pief6LbAYTlnKOS_QNzcEVhnL0bnPELxRd98E7RjGyUra2BvrOWxSwhCzSGXhZOw8LEviCbZ&Z6MNgA3Xeadj0ENxBsjbWDoNGcL2VBIqAmVkfGRz3ctGDZgzTZd1EXtM9mdfA47dtJd_mQLQ6doQ4dgwKBExk_Z1tLU8_ghFlmSbogrRHSAAZf2u3NbmAQ0QKGekdd8CF8AQ0iVO55QskAcPpl7l9MuCGx0tmZpg2cYUba5YoQKuqwjReCjBMem_5gkK0i6AuLap0lUjZQk7WEkq6CGXO1658k4MtVrMeaQu8lOgvZ2ukqioLHYqofBmRusFIExROBfQ5YeEDRrzqdWcxTs8YpyqvK4wgSPqZ7NiGejJ2oOkhsh96Qr7mlgFT2NUSe79q4jVAdvj4SSqR7uo0nmZLdH9JJUg9D3xjlREjmFd1FQ&0VCdHLRZgSLpPaSTjQAcpVmEj4XxFtmLJ0R5q0qx2t4_FW26ZBwMr&F58gKwQMtkXqp4slTChXmB3SwboIBzbIRv4g5alma55JPxzJvFJz5W0ZjZdWEdf7MS6jDufZcoAqW1_D3GIMXK2REHXhFPiLRXRJwIegzQhRbY1oum1WgQKeQQAj9cvzFRcDxDetDoM9JrxhkEsRdSp2GUwWUqsoEYYj8jB6eHC052ChBFFZCR&lLklSJkBq8MCwCqsevRwsyYkxzJQj1pnJJkbaEt_AskahL4eRLCIWAEhRa9CnPi5q8C6qEGoTZKDoezx71eAkvoB_cToTOAXApmekFBNboh1qB0NG8cNFWL7jSxhYfYXzR_MBtFhevsG8wGkZdloX4heUsZ76FfU3d255P5FVahHc_&HXh2F39ggDbCdmVd9kq1B_DDIg2XgKxjkN6ownCfCkZ5B2W98SJdTxQOM0hQvjfOi2lHiMr7i3WvzBNDYUf3UiBgetzGkwadeUtW_vgxNSkgAL0fUIpofVOizDMH6SW&IpgoZOW2eOwhDrEHHQkvshpNa7qAhmVDBBb2IGHvSPjg5phA69wb0MsfkVOVsEQYhMUwQLwsIX2UNPiWnZ7zoIiW0M_W9KeP_LaR_L3tkb9ua6aF8yezvlkE3GF3mbPw&mmeBjJTFLfiSlmP6awX43xpsYsWSMkiPpWcEKmywGpBbelEcn5BAMELEwpxK_ojqvoDURb6jYBY9YcLKQ0Qh9wIirHKt1LUi4pFrD86SX7higthbIZvdiL2giglEvxVeMvlU8ci4CLolog41RfmbiMRI9Jclei40EggImVogA9d2lJSmvOG9qtOLsx7ldXSiocimhSJ0I5IzvK7Ch&KkpCcxkqGyGb8keRAJ15lCOzSKX3s4GjS15ewKWwrKY8cg5w5dhCZh9qsX&kD38ARC7wc2Jfi6xGfX9FSa_vipLyKnXp7fkE_rZOaF4G9xdRJ16TdRpJytEg9x8&Rur7R9inHhmkxNKAfj5dIEQV83_gvhLq4SS9RV2xvwEgOxJ_zTRY3Eem4ZNlEHUKQ5EzQPlMbUrKG8SBFj4NFhSSt0ArpL_NNPBZ5jjUlVJf5ji4IcsgAPUesRxECn5qc5Ce2nyw2qim8AMgKKGmexwWsApvQasVm6RMSf&rUCRqC4aIOQLGLomFvQaQHZ4saeyJEXfPviZZKssRzzLyzhXX4uRcO5eU3LRpswrGR_wQdj3F4wqgcnS2pBidS2_PcZE2u0KCgODnygC1lXGxvvY4CAvveYV9jkchel84HTkw7pP4_&tkcJr&cpJ&QwaLU9qV5mCBeIooZWV4qoGZBSShf68ndeLIgChcPEsyoiUXf6YoRtu6Uh1YcSkxBxCFp6Ss7aDaEaoICHp4v6Evhlq&bbx83gafJo3WISsnvpRS3bHTeh6iw1y4r8il0yxbtU5FCmJCC7cIRRybJnLiITTmtGrbTcyIn9wcveWcISZaCnKN6cvuhneXLUNv5oAu_pw2qZEqpW3SQoldVntOTBLvi0Ua6mFkAgkU363SPJW6K9IsfV78cJlupbmMgG1C&AJxqZbJGPagWp5lSQwc2hPRKe9I8K9gOrCd8VvHEncBy&YOzhObC7f7EDW0HIfOHjcKm0pPg2nj186RtUu1UFcmHs05ATGQ00VrCZvkH4wANqTRjE7P5YSg_DupscsEmni48Qs9oaEYVUrO6ne_IujGNSY43u75kSgRV_uccQvT3GxlFLUnaqFcZ_5yj4L86gAtRKsDYkUWgM6NlslY0Yk_Q6vz1jqwweg40bY0awNXqRXVhrcs4Dq5ZlC5t8CB9gW4zWCUF6Mvasb53hyDlR0viYYF8HH9so58e6rdc6lxbraUM0VDJ9Eie9WiiBkMGf6zhQxQIikDSbGGsj8uoQt8jUFLB0oYUVQor&t1izIup08a6YM3j5AKGpsoL5FSbCvDEOeNwWBxcvvTu8N9osUkKshto6RGFKg0liGIpJBjpwV6hCzTmGHgLxA094ca3yoVK2ZG6LizdBEgAkCLKoJNKy4MMaRlO4jTEMaWw1JCdgNXHAigdBA9L&rfqs7EsWRpQqkji_4PIrqQ3cW5JjRyW_2lYD5FSTL0qVlzdPKCfW1zfGBi1nC0M1_Q4EvRttvV1YIeefATgkE1qPL7nQ_ZwkHCm4SkrOR_3Tqdp5UU6rPkrWnka554eB5Zh2JLgTb1fCc9Mq5WdPD1Xun_XMuLJ0vsF1LaQe9x0WiN7J9oSbcj44rxKzrWqDeGgaP&T49PKG7IN3tM3MtwdOrhj33polTpxik__RHS&40TV&F8w54BqfIjQw7WGDyaCT1l&UaGRsSIu5XEqNcf6CLrZldUobPtTvRFwzSFuqeUAoPWLVd1yd2qzuyJpmBtSf2dbXJN9a3qAFiviRVrbnD1TdeSdFhFQBIltvT&C8iptUBtKEXemM_xl5D9V9_OVhLXuZpCJtr0BRADKGn&R7184UqeYJQoOZX2syEgioDjwkMrlWfoHqBcY8_l8bxJdfRQW9dkrrXzFz0TaSFjYeYjKwJ051xHYXAooYqAHwMSypbDxq2nvghhGkN&ZCaVAv1miz0b6UmzTWwZ4QKlT_zbRMbT78r0hY5C4fW4ol8oGPcY4CH18ummzshMnbSKpH1BMeRFYWXr9U3ctInm9hzJkovv0Wsa_Q_ECOQdFPOE7ekEwOGQUhKk2wzSFHUmOE5GSG1Z7ChL2L3n6YLIuCOYEHYh5yeot_CJnKJpr2mDZUlhYYFpDS7aNz9RFsmggs4hR2TPw3mFDn9CGYiqwN45MQnYWepQcZzjx_ZwhuinlwhaTTWIhfwD8gXCRS2fg3oU&XPtMgBpyYUxVJeLUToGeRJ6eQkY46LOEvK0abmoN569tni4eZK1LtzFy0czqUZqkqGbEh6KmhJ7M6w6S5mLCpl4W&RPR52K27Yu2YMdKbmRZGqNz&yTWH00iOLboQqU_UlVd1o842pdmNnTUp3UDdJqp70gw7VsefKyu&k60YQGp4soDD0_HarBoV9KXbHSicw2v_6IWDB&rymvmhSqD08iIX4rwxlB_7dckAfDrP3CcnQFPd9O55gXTHWQWYvX0W2aTPwNDfySO5AY9DsgyS1N0HZ2XZqS8GCi_vMil3q3Z8fJUy2LKGVLCCzxS5daQ623TbOX56k_LItcBLCk6LPkIVOeurJ_zToDMMjhvVMraGgN9LXOSImU4ZNmWkLdoEZCccTrImVMONuzmlhNeToOhGIXFPd51ulNc8Q5scG9igHM3WG0kqjqqwP3jCj3p37orO1XKT7o&Ouew0p9NDuB5kEYE_W0qITP0twUqtIq&3zXtrXiLF1cdItGDgaJ4BQ58fIdOg6zAHboyXIpVQfoAEn7xeHx7Zrb550jRhMvFNakEWfEDzdH6cmQZlJ1X_1cFpBiTs4YYEOZgGkZIZ6j9rqBWyIi5tKZWiQSXCNXTBi&IANGg8SzP49IJDMnpQzlRe09zovlwYgBS&XnPo&BnJxJB6fC6EXpXlNu3YrIMd78Kpc2vFHZnxhOFwgAEAtror&peFOcLV6DbQd6SQE_hW8n2v02LXmAPRSZPOxW35DLE6CQYCfmFuiFpSMVy9jDy7QRb9HMUkqTgxSRhyEZW_tiEBWqq6g2QoQk45oODbcYnsjrzdyV7aRoSI25lrPiXH3v2YM8QjxlNE2ngfYMvhtTWmVY4azXJnEcscOARls6j8qnXTwdJsRCfzAQVZRhZKCzVRBwO6MHdTBH1OHg7G07Q5iwO8aCvRbZrhlgKQLMD68gNT1OzbHLGTK39FM&YMcwjRpZB0OFg_ETHoQT9xvPo3rt3nUseA9Ti6Zxgxgm5rrhweg0PdB7m0grMmyCQNONjN3cb3B_b7tT9nrJlzmKjYORecPhoCkx_mb2WS9sIIYx37mEQZZHKr9sacHw_EuRZGzdbHvla1A7QQXkcmoZ7KX32xoAfxSu_nQu0MhKxaZoUnZcAZLBhiU5GA0jzSsv4k_y3W9chBo&2G_DyWQwnj2zUnzs26vh9eBpOrSzu6F9nDx8ngy_2NE0zMne2NvJcGgfbu313WDyedjDc5MhnojXwtRstAA99cA&D&82G45n9nE4_TKazWi1q2c7eHykxQdX90N7P&hGLB7_7Xr4OLPf7oZj84Dlv42InulsgBdGY&ttMpqNxp95QYzmTkaf72b27uH_Zjjh_d0PtDu&aB8Hk9loODVEx9fRTfdQZ4MpkX1mv41mdw9Ps4Z4HG4wfrZ&GY1venY44oWGf3ucDKd0fkNrj74QxUP6cjS_vn_64dHgK1ph&DAjPtHJiM7ZA7MmPBtWJ2JoffNlOCH_jWeDq9H9iLbELPHtaDamLXjieCCUXz&dD_gQT5PHh_kQNR2wkBYhhk9G07&YwdQoY&&6NGgWIu7SGl8G42sW1J4gcVz7&PCEUELnvr&BAyY8AEYN7c3wdng9G30l8dKTtM306ctQ_T2dMYPu7_14eE30DibPdjqcfB1dgw9mMnwcjIj9mJqeTLDKw1gczqc_hEdaMvwKHXga3_O0k_Ffn_g8RzQBaww_k7aBmZHczbcRbQ4J7Qu&x6&QF63wn0mNHuyXwbOMaj_rehCZzSx3VytIKVrtHFw9gAdXRM_IySJCwBCI6GbwZfB5OO2ZRgl4ax0v79np4&B6hH&Q96R6JOt74QpZ0V_fIEX6QBexAxInjgY9VJHBBqFr46AjtPe_XZ63e_&pH&Ti&mEKZaNNZgPLFNPfV0M8PRmOiV9sToPr66cJmRaewBtEzfSJjG00ZqEYnJeteTS5CfbEfLa3g9H90_RAx2jnB2IhlmRdawQSlGx60WMdsKNb2ur6TqVnO1b7bO9IFFdDemxw83UEzyP7GLKF6Uh58qArKB9PeTs6Lb99ZMC&_8adDFMNOGuVSuyMgQJ9_AzPPCZUpOHQ41UNoUuKwFmxpSiusKmdtoyuxOksn0bVF74y4itDuYqU02rfBCpJATUzR2qBogPXrtdIRQQdyTQ8B6u0Mt2gIcGyueOD_aVOETS6PNr0lEOZMVyiC6Xbqkq0M9ViqGbkN0BMKVcQRzhl8skKRwPFzdub8DBPAXIrCt9oKwYNxOZ6qVxakclCQhKvbqetLUL5XvFcO5LMkz5Yitfway64MAIMQwEM9s8a3HBGwD&X8pbdFpwq8cQOz&vxQWtpTvCFSAAAYpJq1z_XTpqbRMe&_JPuXet&YuzgX&Qc1siTjfuXvMf5Z3RnqCOvy_ZCY0dKAnPb_2AyJ1kdH_o8dre4nb&2HYDYzOSdRkTtdQm5Xx42uW_bXrzKeXcW_uIQKPePMyDuuGq_tcbwjrRmqwZdkVkQK3syFUKZSwjYcCwhaF829yy0I8hl3IwHA8PgJiFqLLEfe4m5vyP0Th0rBq&wAzbLBXK_uIuEyuvRUUCP9bKdl_iMg&xIfuiByZStdCtbXl4icSVd&Z1YVy&681r&&s1_XEHBeBLKAfE0CCpm4kR5iEAuVwIZOwyllUVOZ5JbgAT0yXelmZQ4O4MZnTnUXvBw4fpIAlaWzehuln4Xf2h4zpGeY&&i5e5EZ6KVjMjp4NTnnND0q8D4oOJ&&Lm3Z8swZQsbZrAuucr_2wtKG&Ta6OBq_nBPiOL_OUbDl6wVqhC22pGK&50vrL6967eGse8R2ujB7txl2Ad83XMQvILemGoKRSH3uoy3W7yLCenLhMp6t0VGx&2sdrY70Mc0NG_rBofLtp07JJ2E8eQts4cVt1C069Huxy1ij2rmDpUM9Na480sJGZcSoitOR0nTG0tSkWcPMHdmU9CS7xdEwXeuYGxcXhPD3Ma&f4&SHmfNvk6lg9tc89e7InpYnsHDDWR_xJFPKXb02nm47N5MHevbG1deWLm_XRqPXD2TnkYuc_toKuO6XFuFay&anLX3UQKCSFcmx_14L5c073QePcG4xDajsMHDUvwO1FRuVTwXu2K5y134lR6IavNds5GMAbUEsIUAY6gT1s1pob9Hev4OjTAeDSRr9HKL11sdSMG8i79oqme02Z9Bjb1LFt9dyU7wnzIxgvvepCWzHVkaxc_e&Uhoq0wz&hUlgB3yRQ_&o8On4SbXV9IgreCe8I9NQUU7RG0xA&oTy5fLGCa6&Nr8noGmnVbGrihBM7Ys0IuGs5mX9EpTjTFhDJzvYcLxS7TiNqNQQr6Vh7jiHaMKum&GT4wuHqpF4hTewjRouMm9JEgW7skc&n4Lc&z3WxwpYv4fUEsDBBQAAAAIAEAGnUcxkLdxYQIAAG4EAAAWAAAAZ2l0c3luY2hpc3RhL1JFQURNRS5tZHVUwW7UMBC95ysG7WFbqc3eQOIGqoBeoFKRECd24kw2Vh3beJwN6dczYwcoRZx2bT&PvPfmOTs42cyrN6PljM3dmsfgIYfgYAgJ6lqPZA8KLsn6kcAFg4KxjhgWm0dAeC8&cweJYmCbQ1phDJypB6mI8IW6GzwDUzpTaptmt4O3yNbAu9mbbINHZ&PafB6ptjdhipikOm69epvIlLI5EUEYnrLbKCSaQqbnUL3&Hx5wm2EJ6YFBViss5BxcoO_Bw4AJRmS55VboiMQWKnK01yVkIWo&3QPGCHstYf1JSMd134KKqPwtS1PL0AdP0K2&dgWq97OdpCROkcF66IJoUMLcwkdaQGnMsS&Uq9HihwDQ80Apya4dRPH3WdT2LdwHUMpSV1DS0svA5hhDymWUWgF6cqRewzJaMwKPYXa9iKv8JvQzOlEbNjK8iuCJBSAVqM5fuEuv7Z9OwVDKKPQrRYNe62lnGR4LyZkVaE9eSxRQnf5doo38RD5z03wNM3iSGxK1Ec9ULNoSuU3NOCtYMUtcc66olvlO4qtTAZhhzDny68PhVMLYit_HCZOZ_eWrAyGvC3U9nlu4c2hqBzbJxqwTkL66cZT00nVE84An4uOfNLXwxvdXRXOYE9MVrM8p&5uv&bQ5oKX&Dsrv&FywqFDmQnxDKECOioDLathtVY06wKY8FBYaRqPWl4njGa3DTuaM_myY3HBNPyQw8r6k52Zl1VudK6E4drN1&eHph_Dbo41tXI8t3ITFu4CiUA4qXnM5BOfCUh_B0EpzecIy&uA1DOqI5tB6of5BjRlm&6L5CVBLAwQUAAAACACWAZ1HmgB6rxAAAAAOAAAAJgAAAGdpdHN5bmNoaXN0YS9idWlsZC9naXRzeW5jaGlzdGFfaWdub3JlS88sKa7MS87ILC5J5OICAFBLAwQUAAAACACWAZ1HC8Yq9hYAAAAUAAAAIwAAAGdpdHN5bmNoaXN0YS9idWlsZC9weXppcGlzdGFfaWdub3JlS88sKa7MS87ILC5JjK&KLNArqOQCAFBLAwQUAAAACADtBChIg4PeUfoDAAC5DQAAFgAAAGdpdHN5bmNoaXN0YS9jb25maWcucHm9V1tv2zYUftev4FIEojDDWF8H_CENXCTFkA29YhgKgpZoj41ECiTdJf9_55CURMl06_5heogl8ly&8&HwRHa9No7Uun8uZHi3zkh1GL5utdrLwx&cWGGKYbHVh6IwotW8ofBeFcWh1Tve4sYB5cIv2eDCWvdCMVwBsxRk65ZbS15xK4JxqndfRO2qX4uCwNOIPTkId6&cjYNQdkcnLLWi3YMAiY8R7mgUaaV1aDFRe6V1K7j6YdXm2PVz0fiDa2s2bq_Ie_5FkFwzpngnGCM&k3JdVqki2ky1ap&qivTcCOVYb8RePi19zVEkyRM&9toQ_iieV_Qrb4_iIlJFyxBLI2vH2Fo60VmaZDy_cACFYfhQGJ8F4IVrdAgOLFdTVqMefoLKLHRIGaRHkRc9kMZNHsYNuU&cQrS0BLlyRcodFAp&gW5lEiyJ2a8bsTseaHltN9e2JNeE_jBWSE8akq_qUUu0VqQ2kqJ52VXIIZYpMjCw746rphVmIqEHzJePSSUB0VkFGaDbt9yJGHMxulvsA2CLlUk_OrA1V8yCV6lVdBK&HnyqnW5EOxwLLL3ucRNhTD3uZSvWYQvZPhoYNH0RlHaJurc8UiY5HFxaQbZPtfCi9Cq4OBruNdETZuW4VBbsALayGcyWWCcfWj1_X2Hhwv4st6pKQluGlT3FCUWC&EesK4Ac2tX62PdQxBNYwBadYRqUE_qMAUSDG1K_LMkI9rT6&u2HbXbjz_277Pqnm7u32Y03N&nlck7hcDY9JkPcK&LeAPMT3mfC&yVr&fXNb_&y8T&8flbh9i6vsb1&yG9cksJrDqf1&Nk94eB95FkkBbS_R3A30C1ln96fsu9iSkwBZomaQD2j6vyeSmjqzHOaFrS9gbLw_l_YehbQwfQYK0Tr4ZtQJNySy1BWx04YWYcL5v9DmWSeEfmUIGcw_AE8i9h_jeANS1RiC8ZXFdrnGMTpxez&xKtKqr2mV2gOOhHJtEwPGzbwsDfBNvhKporlPTLdxxGlZaZAqHRIW6cfNK8Sb4snCKkLLZS8IB1&FBEkS2qYzkBNWenk13Bzxdg3fliE61n0_JKPORBRGKMN64S1&IBhPmg1DAbF4oRgVJYhhBjPMlxcp38NYH2uprsDVuikW5GfNuTlxJVlAFdbXCD&&I2wfadeWJ&B4_ko9s3zdcatZ8HFvqmfdEQ1EZJEWCHtmYfB7fJIz4QC7cMYEY_Fp1V2mIgCvp1NWH9Lbah8ZqaYnWXg4nHHRiotB9DURZUceXC0GJYmuVVictLJ9o6Tpnd7wXiz7HX5GJeP34j&a8R0090CGxBcGI4OE2cPI2noLBJHz&iPBV6qjHUQEGP_bg06RfEvUEsDBBQAAAAIADwNKUgnYyyCdgAAAJYAAAAkAAAAZ2l0c3luY2hpc3RhL2V0Yy9naXRzeW5jaGlzdGFfY29uZmlnVcoxDsIwDIXh3aeoxA5FSGzcgq1ClkmtJmoaR4lDlNvjhYHxve9fOr9X_rwAOIvzuHJUmh7T7T7PAEuxtwaVMqxIdLDRFrSO5HyoShDFUcRM6k3OUPgQ5d__&KXUVLA6SiZXOHUpe0gbOskDO_3cssGzNAb4AlBLAwQUAAAACAAiDSlIbxYY9AsDAAAKBwAAKwAAAGdpdHN5bmNoaXN0YS9ldGMvZ2l0c3luY2hpc3RhX2NvbmZpZ19zYW1wbGWtVU1r20AQvetXTJODm0NVQ6GEgg_lJiXQlkASSglFrKWRtWS1K3ZWNu6v78xISuR8HAoFX3Y1897MvHnrU7hpLAH&DJBpO4dQBl&bbR9NssFDbfmqDhG2NtHBlxydTA6&Qg_dMyVyXhm6A4QakiBpvPUp8BGzU6hsxDKFOEZwfNc5Ww7gqTEJDgy1D72rwNl7BM5Unhi8&YM5Q9w06KGMaBJnezCl5lITYir7BHubmuPquBzjK2WTcrxpcWL3uD9ukPG1ZENjfKQEnYmckzDm8N1wTdRH1Dp7koYjOs7dIccxdR1Dq7kujG2NXAy9tUdVURltl95kQ1OCxbiEKVm&pSntJ27WZsfXcccFZHd73FRm91uSjj6B9vX28gpYnfWPaz2fZcPHlRTjmkBpltfxxMBUVUQiyOS0Ol_eLyXiliZA0dr0XIhPo0w5fAlty2cIPG47yngUAg3Pb4OsU2XJbBxWecazioq4goSUCjkL1ZUh2odY&T_mbkIcmabz2NiwmA_ayoYldE7BUwgOmrCHti8bMA2aSnWwLT4XQ2xiefOQN6iicTVhwVT3LKD6YDGFEmJLQrXBEdZA3Tsh63mtrtUfsDOu19388HG5nIB5o51j8DJE8Y6W&2wyqq_uLumyj4UOF43ZqY_JF09ytB3ewbbjqrELZVNU6JLhgQlxlt1FviUrPtVF_xa2VvDn1nkMyWaySvT6wePz_LnRrderq0Nq2NZcyexdSBExh3UAH5IazPG0ZJ6L94s80z4LNdq&EAb&gpfggjfuiVwzMpAvPEHP5WQR25DwKfFn53hXUjSeaow0eH_Q4rghUX6AmGp4_J5nU36RQjEGreAm9vgqxStQwvIS_zHFEPHI8PX2kufjDp&EWqE1Yi3nDvA24rszKo0fDPOodw6XtarDT9WTVWDf8HvJOy55Hit59FrjewXcIFtcHkx5BMU8nEWWPZtnwlwo1woujKOhdaJefWfSy_aT94w5Ngc4mat4wn5CLw7b82vdd3zZtvoPMLhsAMjGlEJSijHygT37C1BLAwQUAAAACACWAZ1Hvk2692QAAACEAAAAIQAAAGdpdHN5bmNoaXN0YS9ldGMvcHl6aXBpc3RhX2NvbmZpZ1WLSw6EIAxA95zCE8huTEzmJJMJqVihCWBTygJPL3Hn9n1_AQsKpL8BZreToNdT_vSdAmntxUeqCo9skgaOqlxXa4eObZv9mW0G8a1_FvtaLmJ3UMICGce3NUr7q3CjmLkbcwNQSwMEFAAAAAgAdQInSAXDzL&&AQAAzgUAABwAAABnaXRzeW5jaGlzdGEvZ2l0c3luY2hpc3RhLnB5rVTLjtswDLz7K4gUQWSgENAeF8ip2D7OaU_LheDatFeAIxmU3TZ&X1Gv2E03vTSXUBQ55JBj6fNkaQZ3cZWOpnVVNkc7ZLO1ptfl5C6mVbeuzbXDEdvZUlURjrbphEersx1zy3GFt&FtAzJiXQFUHfbAVylN9XpE1ZhOcahYOU1zxvqBUwCG0X5vRuY1IEVXinzxqSMSHJNDfgh&n6N73aA8eTveippbma0d1SqgYGRQSbjt86a92ErAYDSPwHao9NWfxZ8lUsJMFyYW7FW6dG1jRJ1v8FeL0wyP4U9bA40DXOXFaUgksiR217C9g24hbQZgvB3swc0ksI7AhPNC5h998Cr_Zx8eb9tHFXTg5oZmNSxa3Fl0acv58T49V6WgNr0VuxNjcJFP375IKXd10YbL6_h1klfaggvcekspELTJKbe0YpWPdjFdClqoCfwOe3fgip5YUhjhZJ32Sr&ILI8EViadzvdEc5UK&978VR7rschmmtCkb4099brSne2VXjZUH3mPgRz8fPFCh4lsi87xjG8HwOxFWuzb1_YAZRL5KUiky9MQ2J&SQeTvKl9G40rQlZfk3GhzTzzR9tW8Ia0fk2KPp5JraP8aofHQfow0&KjheIT3D0UCr71TOf7p3TMD4ejSTFeS5gIeXimegVKMfFCKO1bqwNGxeQ77DVBLAwQUAAAACAB1AidIwnwiowkAAAAHAAAAJAAAAGdpdHN5bmNoaXN0YS9sb2cvZ2l0c3luY2hpc3RhX2lnbm9yZdPSy8lP5_ICAFBLAwQUAAAACADtBChIa7k8Zo0BAADfAwAAEwAAAGdpdHN5bmNoaXN0YS9sb2cucHmdU01PwzAMvfdXWJ2mpBKMO1IvCAZICA6DE0JR1rptpDaZkoxp&x73K_02uCBFbfPs9&ycOqrZGeuhNmWpdBmpk_2qkjqv0boRd0cXRYuyNltZd0loIYpyLMDsUIuBxpPbCIDWSWIPqQJYv2eg9JDhegaARb_3eiQQtIDMovQ4aQxV0_CxRP&SYZyVyrujzirlvGRJSA5tEOvza4IdMfEbaz5K3T&cfTwmvdFQOTPamRphEAF6ATGhbqngDeS43ZfEKKqZq7Wq8aln8Lbhm7m3FQHsChqTY8oOndOi_tPOv8xkczMbT_xmtJN04ctyz6&rt9NqhbGN9L479&A9b3LEOFty6TKvGkwcXMOSd4a0DPsGnZMl7dhQQub5TJOcZ1XwNemGjOmMfg0GSeqbtM6mZUWRsfusaqUWl4GiGv78EFK6MDzeeDndh7jNOJvRdvg9Oh_GPgzo6ZWYhNFaY3n8TqMAtKSGDolnKQdpdcuakmCA4qQrQg_6SUK0JywEpCkwIRqptBCs9dE7iqIfUEsDBBQAAAAIACINKUj9_KyDEw4AAAw&AAAUAAAAZ2l0c3luY2hpc3RhL3N5bmMucHm9G2tv20byu37FnlpBZKsjkt7hPhhQgcBJWgO5pIh9KHp9ELS0stlQJI_k4hjX__83O&uafZCSXbdFUJHL2XntvHZ2Xe7bphtYf9&PSvm4qUpeD&qtMeNDuef6eVsMnL5Xzc1NWd&o1858GPi_3ZWVeb8cOoC7eDcz1Jp6V94QPPqxv683ufv1ruk_wGwYbe9ns45XTbFNYEqqnyXr9hVnm1eC0YxRlOlsNvvm4iq&_Obtu&ev8tcXb16xNVtmN_VQ3tRNx5fi8_UPb8_&vbi8euHDAZigcFv2Q5FHJ5y&e&v64pv4BMnXcjZ78fLlxdXFu7cv3mgC3724unr1&u0lMvMFgFz_67vv3r_6vHS&ADr4dlM110WFC8K72Uz_wnd4yJqW17laqkRIu6mKvmevYX2S5vpXvhnSsxlj8G&LdyzPy7oc8jzpebVbsbrY8xVrb_&7clNUuXy9LnquHvfCHlasP1znYsF7oPm2qWGk7JU2tuvXRdVzpIFUGBOoMzEfoMWPHXQIwVfn3YIZBgDEPNvPyBR8wl87TJk0z&az5Ri_2xfNtlAOjG7LDjTWdPeoIJAKv3d8OHS1T_YvUhkUQ573Q6e0q1Si5s5hidaLHkUWv0BI&AAX4mfRz9mCJUZzq4i_VkYOy2S68oVboUtnG&H&xKorTSWbgslNs2_Ljksp8ut7xJ6It_crJn6_QtYV45t9K78pxhAAnwVKZW0XSPyi3jXHbU4gEGoCe6VW49q4GS53rOJ1Qiexr9kzOZGxthgG3tXqE6xssvxlyb6kRLKOt1Wx4ckyW66WP2XL1I58sVyh_5Ghn2qA_vy3X5YpoFl_Tj&99svnAn6ZKuKS16wUYs&POw7xc0tUwe7K4VZzCOq84Z&YctEvxVK7fGuEuF4ScA0TMrFSwo89aGa0w8H1zmKThWFqIGvdykaI89MVAFVbHBorNX38kO2LYXOb4GTHBSgvahaGBklALq&iIBcqAy6J2YxHyFTP7Q9t2&G_j8wOgmdK4_CLzQamHbfMrmmGHHR9G0Qz80Wsi362eETW8UKHCqMCbi1DpvC5esinIiesQN0MdqZWpxkQoc3hZxbY4RvgRbiC8ABmeDKGZ1BJm9MB88efpROCxUJ8c1cJKaKIZDxp_kygyX5tyjoxWFfMS7Yq8ETy6KPRR5O1orNrOgamXkOJk1VADBRgZ6dan04uCNaFAY5QESTGJrtUwURlikAGxj8K4xi5C2VDnrCDMQUZOIgZnYQD&obErrmQ&6UxDIup7IW2HLgdBdXaw&Hj7FpwFhQQ5hMNGj6gNQzrWtappLShU9lHLYVLY4QV9YNes5bVkwhxSMZkANf3ROqAfPA89SooxZqpXNY7VUitxZLAauR_WbU2T05lFYqCMFnRQs23xZyY2uChYq4te2zox2zIP4Gh9io4_VFOTdamoGCtLdBAR91UYlMjyJAqmfx07mQYyo87V9mXHFNpz7WFsh4alQidubGcrGOhhJOLqwMhnUsMQCmC5BaPmXQs2ZEpqkRQSuuLj0Cna&aabbsEYANBIYRVg6jqEwkxv7uep6zokf0zYgjZXVcOYJSmhHAWiahpeskJpQ4ogbHDFspZ9Z4rk3U4l3WlRAh2c0AA_SlRBq5KT_veFOv_gwg3AW_ASn5xjE9l8_&59cviI8np9nEir9&x623xMZcbSZLmMTE7uf7Q8i7xicgaO80MVlsn2ArBoQEG67xTsSd9ke58tC_KMazQLUXwIwP547Of2VpsFZejxVfEWEOep33_9xQ3R8r7J6t45Lo9uOZ5_mLHFCERLVd9rB7ZUYHXTG4Cbc7aNPVQ1gfOqHbGzGRnNmeI_mipM1KVGBonVDBR2NHSwEIrHj9rIUwNSmqrErPTB_tePqj4sBT_4CJE79ZPKUMY042LZw8pTJhIEYfNkKvJuL2HoRbjrdIRlCKLYsUWW7a4Zosf2OLbs8U&zxaXbPHvZUgfUew&yIhukYsN79&_8UxzF5RCUtiHFkNaRbYc8vtL6z_nHHpcNh6JW04Auiw_ivijehBDoyLRmezqkESBALlSrO6aZvohoc2ASOg4tLLjabGsDPITU&_USMe4G_Vr29zVyBnVISnKosF6aXS0ZIJhNc1VmE5WQ0elzm748LGoDjyBeHtyiXLCat4VXS2UNj8vapGVAKnyGRHRVXpBg5qbmuaEiiaiMr&CQSR_by4H_r3sfG3LzaCac&j81Yptbov6RoZipCNYlMDCtRTw81SkIYsig4Jx3yeKMZV8ZXfPehfJSvqzxOng_oqkJ8tKVvO7PHDL5&GtGLYSwdYszh8tsZ9pwE8EI4lhlDRARcKRLUkSHqBcrrdKLrmAXysgfKOxnvK_b7blruTbEQEo6JbDNs7w7cgww4UcuqLud7zLXaQJQQKu0hy6jVrsQtWaFnPh1LWRDdVOyS7WZVyOoL_EEnlqNInSkAeZxgXGdcLArpfJcfIrJTzGQ1GFiaCoqzFJ3mttG&TuhzT12VJayYIwPoIhpuRwI&kgyibUjJLEMRl8ZsqxjT0YB&nDTKFvugGKoKhXrkQ&fx09AfAakdpIvKCgS1EbtoyS&NMdXZnC&L14cKvoQK_klDDWlaazkCNitpqrz4IILrrxZQPb253ZEJRQWmFYh7IRVcTu_XDGNti4l2a6L_pDUVX3wk4tE5qIJ3vY&hfmHm4&QuWM2pbMC2MTaPR8Cn&7Xa7253rZhIOhex1acXqdKy7Eh34o9u3TOpkkAjsBPUWU6gHn3mYhjU3UWWNffOB2AOy1gBkhGeUFYJmGLG5ezQBs3geRq8azQHoM3IQIU0PTmGKmhqcVxk8EXFxSz2iNl8r1sH05ia85QPJGXHigJlCVtfRmhBR9ffbXr9lGVmmSJDNrHvVdz3Vnjs2BOuN8_2kOJLYxnxYWbl3h_CZiFn4p4SEeoaTCn9iiF46qDn8NLecIl1i6M_7xkRpPijii9aXp1Gszlmq3naN9nHKsG57&a3OyjRZ5Gu1Ypfcx8A&cB2tmZNI67ZC5aoSAjqN3fN8MPHD1I5siuf33kOHVC2&MgoeE8DTXHxzfG0lYkknkJv3Q8XkaJRMnEItEIxRRmmMErchRBcTJkZkk2sB8YluhUKeAqiImSWd0D6ZHjVFGl3Eq&PqyxlV_HAVdH1PGhPu7GGurOLnViDbTKdSTSEYoOriVYkc2NDmkdzkriANjW6C4ECFfBem_R5zKaVKH5fUpjNla&A&lydMYllKP0Vm4OqOMjHF_TGkn8eap7anZUrWcBCKlnM&PaM33ZIupGLqB&Fl3ebOzlnUN8soLPwFbqmklbi3FGSGlFvvSwoVqjNRk4_yoCuYR7HiF4hGe&LJyZm4X4VXMjv&nUHbjfEi80xoVLEyAaUlTvAlmKzqtG_SjP_z3hb3GR4tWfWPO5dfsJdWPvrcn8x2UaddcbRW3bLFdKevrz_DF3t07ItfqRLEsu3bL57EFBbk6yBI7fpBkLqGwDxnLSWr7b4bt4efMbfXZgp3muf&_z9sRkN1ArF5WLTFn727a_lrVo4xm5ATAfE&tApHmPn6SsqPw28O_VdFJISjrLa_H9bP4zm5GzusIc06ZZG9oztmcfaEwYqs72enSG0_s4u0JyhMVTeIR91Hlw5fs77qakTXvJSzsVdNUxwveAaByehnaL8h9AHEO5A0FtZUuwMxxFH7kXdd0wSi9dJ2rFgtzb8ha7&Mpi0Olpi_F1lxEd2Ahh&bM8cwpcnQ4_16_nMPzpYRI4tRlcz4MssU_zIL0AH1KDHOWqRBKSXJ1DtDz7iPvRqNTTLqzY_JnURLuTQ7YMwdEp7Y_wVoP4h6Yw8k40Yn1luDZAeDdo249oo9ej800E1vwF9DK9thEDacmuicShLpzBEuQk3H&zoc63DnHn0lTy6SeVkys23qaX4BYGUac&9quGZpNU62Xt8PQLlcMUJY7sIe_ktcvVmzDu0Fd0dCyrfXDyoi11g&2FlW4431dmls3R41fzqfnW9FNcXCdx7upc5SOwoqElOFS2&TCGO0gnNYgsPi8bbPYLstsMTctTBvkA_LhftLD_F5u_R_CMrq&jDIKZaSP2TkvGOE2WolaX3EIiQGZIjEnAmQalVMypGvI38tV7KDr0aypJXiwsqbq9qdh6XHqOlq7P4Q5WYx_2vB2YK&wR7Rji55xr2zGhJEP&JMIiAKBfzMTAZL5K0ws2wMeWYi0dKaIWgTOX0XoRGQ&651HcRAnDLHEJg6Oj4YQMx3PjI1K8MAZJ98WfS6ZxsNms3sQ7Wcs11MnMyMnpFTFtAuk423SIL86ZYAbvyTUGDFnIuHZvfhHd&P3bkURzeNmXU_p3EyDwLReyO2mwD4nWzbpKRNHO1FTs8e6C6lrxw_VF&E9UFzabHmMwLH5E_nPtbFTnNkxUeLMZM_vvGCqSnbYiPzR3Kmtg1Ax4Sae4rVOMIVQihdhS_wAKLWT2fKRnNSPiHis47iEWfqZV7ShoUPSBAZHfwF3qYu79w1Cdx_UwnuM3KLzMJNXm_st9RVy1XW9zLKl3r7Kr2jEog41p0Bqln6dqUtNsKGW1wLgAeFlTwAfU&W3PndF9YFezB2aVlxLW191B6hzYWWF4lQhvGuqqrmryvpDH&4Jls6p_kDTUPI0oXoacrOwZmN&Euzc4XWE1teL3D&kMbJquJSRG2Ihez5WSU_NQubfVviHwip2nePPt3KY&ul0JhoN8muiSpHCaxa4OPGvBHJCPbEMayWp5dSCOgiNo_q&MpWw2pIGiMqJNpfQrNTsUnRBBM08x0vCeb4vyjrP8bKwRDGb&R9QSwMEFAAAAAgAIg0pSBs5nu9VAQAAhAMAABsAAABnaXRzeW5jaGlzdGEvc3luY19jb25maWcucHmdU0FqwzAQvPsVgh5sQwiGQgmFHJqWQi89tIUexcZeJyKKZKRVQn7ftew4Lk5bqNFFMyNpdnat9o11JEprarVJEofaQpV12zxJSg3ei09cP8HhMYI9N1_Bxw7J7xMheFVYCymVUSRl5lHXkYiUEDc_NOiy8U0zEUXz4Uyvb9G5R3dAJ5Yi1bYEvbWe0gsbPS&FolgUFzDwGQN7ZOLVGhypuYajddWEwMaWW1mhJmDu9q4ozobbWjZIL4YeiJxaB0I&rskhBWdElrZO0plIR1elnFsf3BvDXpF1p1&C_yu6aPVqYTEa2QBtJ5TDvSW8zpED42t0kqzsdCz5cOEHSXxlooDAlC&BMPMM2o8oznqnzEaWtjnJI_wwNIPoku3KWo1g&sh36rVNe2KvBQdH7eaKB_6LGL6_Qe8nU&53rrtacV3Bgcv79o&k40acR4BFk3nI_YXkC1BLAwQUAAAACACSdChI8AfshtgEAADcEQAAHQAAAGdpdHN5bmNoaXN0YS9zeW5jX3NlbGVjdG9yLnB5xVhRb9s2EH7Xr_BSBJKARBi2hwEGspeu6wpk7dAUewkCgpZomyglaiSV1hj633dHkRJpy4nbDRjQ1DJ5993H48fjyaLtlbZkEFkmwiMdrJDhq1TbLNNcKtYUfqoM32GuzLKtVGsm0XDLdZaNn_QGByrV847iiOi2BdjWkhlD7vZdfcclr63SAbT6U&BPL1VntZKS63KVEQL&Gr4hlIpOWEoLw_XmivRM887Sx&rmreq4M3SmhJih57qI0a8I_pTVBDE5l6MHzFbGGfMGbBr_GZgj7jzdq37oweNowuUgNxCOGh8vH2GJp4Tst9zSKUKrGu6WEdMWm2UeY7yVR9TcDrqbKXhnLs2hiQPDSOZ_Afch88SEoe2estoK1fnUGg4WOuY2QeIEUkLDLFreCB78MRdWKWng2e4lh5zlZse5zQHUuR2oZd6EyRV8oi8hmbOlZWvJH0EtNEk9GblVG1glNcPaWaz3tGMtL&ITTnkkg&VgreqoqVn3NFZkuOQP_Of5gyH4n61DKYylDbOMGjXoGnM7iOoWRn_BwTs3Vtw&xIhDD&bcZZIaC4_mKI9mx6zEs5H2NYeth_3FzSwTyXbKeht&pAAmCNGN40D1icGxAy0yGWN77SzQOzwbqVym4fF7JbqNKi6OYVYkzeXNpbkglyBJXSxkuhyZCctbFN&9w5jBDWgKMYnoDiXq1_lXi0MVG6xykihCCfAfnmrD18O2uGBNM4LmlyaHJ4K7itwcCNYKp5EygEjR4UZfXMKaxkUUB5ZXs_so7aFtmd7PECmPMWUI65OCj14zUE2g&u5&Zz2E&JvkVljJc7IaWXxJ8UACLvCOGcq1hkpehu2fce5z0bItzx_wEECdEbXqzLVQ5qfrtZL2Wg0Wsa9&&CGPyuZY10IAqFOY1443cYR4Fpet_V_D0KnNWTw034DIdzGVeRlRcT0Trt7x_iNswMcFwBTuDDDDma53CaUsy15MGcAiDxl407aDK3ArEiYJicwk7wpnWqu2hbAl_Zl8v5pNZyasrrkxSu_p3feeUsMtE5KOVSufvY6FPXm7s4MRncxRZS48Cna_IIOO8NhVrIdOoSkCkwOrF4sFsNqJ7U7Cn6W1ku4GgKrCBmlN9fLd7bv39PbN698_0NfvX716__z9UcXIoRa4z2dv6u&Sm&rsKBOMVp&ClZFCnyqZcc3_FyUzgvmmkvkVSQm5CTV0Wu9UVJeblUnEk_GJgoBDrpt5xIL5K4OzNs_h7zSXIqXFY&GkptAf9HAKOY0aLTzGy5ZAY89TmIutSsU7VFqD65oRF7uS2HQOEdrBHesayZ&rB0_Iq5bKpGSxPkMJKTwEdOB4_inFHjJPm5Y8OThHXdCIkByWxas1WQDZaNWSNM6xxBsn8QV5x4ROtknR7roz4GjiKt0a4y5vdS5h1zyOnhcJCf6Z1wOwQINiid5xj&c8&efJY4t7PnnsnJ8kH7dH&wl5oO6kd9x4uuHJONSohV6VHM1Ux0ch2XA8LcmSznyhO7wmvq0UztXrsNtMeKFO&i9eiUafpDtl2jcOX1t3TmgytCFQKqZD7gRusc9oZgssJiMl3xqFNYfX55NeD6GZmsv98ZuR&_UgUWf0c4J7rP7A&9NfP4r4JS44TC9jPvDVKH0q2ZrLG2caDQDCP1BLAwQUAAAACADtBChI&fQRx30CAADMBwAAHwAAAGdpdHN5bmNoaXN0YS9zeW5jX3NlbGVjdG9yLnB5dWndVE1v2zAM&SuBTx0QBZYsxXIxFLAdZzv01BbboRsMxVYSYYoM2PLSLsh&H_Wk_Wy3Yt0usw8mKJIi3_Pz&cortGga79L7pOTS63vC2lpNWivBt&KMWEg4_w5n_UzZ5tEUc9VYAYFWGZsXla5qCLj5kMQX&sDvnr4&oCF3Bn7yPBnvIHEiim_zumpNeZx_Fvx8ujRiomXpXdq6lVCtqktZv9jIqXFYaarlA6R4azDrzaCrld&v_et_b0Up7vcoCdZriDRV6fC436N1LSZSn8E1rQCTRv2AUjg8a9XKBwupJzh2OVuc398_NlYuUFLp8srdu3Frdxk_6PhNY7s2&ihRaDUzC2ncEFpOLbjaVsF4XshIGkZjirKMYUQDjFE8SjjyfZLxmA4xxeExzMN_b_hgxgwAD8gRyl&X&T3Qdw7CZ3fzjXv0BgRLYUXeVG1dyNy0iwmUqaa5VsY1hs9437L2_SOk1tUyn0s1mwOIlB6XEoVVlYHIRurpYC5MqXfO40gFS_LAuamWPfzFuA&pXW2MoHehTpsspZZW5id9bbfLOmencLeWOVwuCwuY7NhlLE3idBwgHLEI0ZRgFIU8Rizj4zDNUhyMxicXHgqBn_orpDuBkYi9TH3SWtuN&jre&cGQEs5C4IwTTEn013k&nIq5P6DVbqhbp_a6Mu7gJfKv79wcvyS4qz4B5XuXU6GbPUGTDoeOHQgrqtpA&7UoVQt4sN1ES1Xaebd&W96yMcckGVE0iliCaJQEiJMwQSSNYjriGQPPsSoJD0CNYbhTJvX&A3oKYf4pL5v6r_cl4H4WxhlGPMMjRHmWgRUxxICTJAvGIxzQY14wYb&hBd6fUEsDBBQAAAAIAHUCJ0i21zel2wAAALwBAAAUAAAAZ2l0c3luY2hpc3RhL3Rlc3QucHltUMtqxDAMvOsrzF5iX9x7IadS6H0&QLix7DX4ERLvoX9fO0rS3aVg0GhGGkkOaS5LFbF4CAynkl04s&UnT7hTsFAsxspWrA7M0pk_lCsAH8u3id3c0wLAUYyd0GWmjJ0J2ctWa8mJSmuV6h2EaO_5eaMY65BdkZdrNW2&3nJRTeOheDPZxm0IE&pjC19MP_6nrw2zKpXiAatJc6S94PQ4TPVCxu4iuhBJDlSnNx9qt72FtZpDZaPhP1tt72mW6vWcz2z&joHgBGI2iRDFOIoBMZmQEYf_OfxNAL9QSwMEFAAAAAgAdQInSN&tiY9BBgAAxBYAABcAAABnaXRzeW5jaGlzdGEvdWlfdXRpbC5wecVYbW&bNhD_rl&BukgjbYbR5NNgwB_yNF2DtUnhZkuBYSNkiXa4ypIgUkmDdf99x_O7LCcpOmxC0Vjk3fG5V96Jb9umk6TnCde&qmaz4fUmCd6TpGNVk5cp&M6S5MP1_dXpG&p_efb6&CNZkIm447K4oZPkx&Ornc0Vl27&w9lP784urs5e0dPLi6vl5dtQCNtsWS1ZSYumll1TKfr3b8_v6Ombk6Wi_DJJ3p18pOoQeP0hSTZVs8orRMy6JNF&YQt_zJqW1dTokgLokq1J0WzbXjIKkOhtXvUsFTKXbEqaqtQLU4IriiKbJ4TwtV4gzxZk1TRV6ijJiwEpIR2TfVd7YeQPTwIErBJsnBAX9YM4BZNohJzXrDNI3fuU1PkWgOKyBblhcJDsdqkumpplCr36oU8X_2i1xAhp2&FaksnZcnm5nCMZOTwQh6RuJFk3fV0SXhMnCPcm5ICkWqC8bwPg2YxStU5phrITp29elnTLhQBXUQWNr8BLIm1Wf7JCghi2bSuwIyoL&4qbvN4wAY5_CW&rpiOKSSGxlHBSyQtJqdYCDKQAWyotd0Dj7WKPVS9TZ1krWq9nmWHyWOyv78lR4lxsFhPrWNl0jPKabpuSValgdanMj29WO5MsaOsF0SQz9QZ7z40&AprFZBqyaBkqbP3aDKKwwyS8SaP0NHHbS17NxmIOcUXipxaQiRUMlv2nDeuBOTCNJLpszJS_oaC24jL1NcDa3FpBwVtgOCL7wkWf2tgRjsw_NxcQCTK13h3TFFMn_3oLIfFIqQkMF1UchcPDdJGFjnzIuPuK6Td4VbAKQh9KMIfXzy5NdyrXy8SH_FGSFFUuBPmVs7tTXborqAUmj2xYq&CnIBcUpWCLaj0lbd5Bwae3wLdAY899XVAUs4AA&BW8eRJUhujy5leLG165ewTAqPz862_&byTGTKJfqXW6zdsB_V3e1VCbrpvuU96pqncuRM9KoHqdg2ksalvKhqcbdbWlh5s7Su9g&00x&o4VJt4Zhb6XegaxjsZLsxAw3usaIIpQ7DuYjL16PlPkWoqndrQqVgd_88U1Xp_NGsrJnCJDBNTBx50AoYlDBzS4XDTnGqKZWhOt7vGAwCehrLijCBXDeszrHXtbBTXLrGSrfpNOxo6cmxsTK5a6NvPihql6hSCMmFCZHa8mri54W4dGfhIGWCUHQgG4LUizRq&DQnBtO7l47biCVDJRQJnIfUYi4dgxx6mTMY3UA9RDMVFv8mBEDzgdg7HZ2LZqDjDKnOt20ktXZJFm8716Is_ooun&qdxT3I0o4pbtWRxzz&dCcuXRYHDvD_TVcVBLovTiJtIGFjHLM93uLJBjPlQ_MIi&igw39piKwLeXSs7hBztOmCvp0HO5hvCh4h6SO1Mb2nFjH8&J9eXy55Pl5S8Xr_ZEfOJtC8SES9blkjfQeN7CvWi4hMq9IUjXQPvsi2A8chtddcEsEVvKW9qeHyuoEsXsYGnYT_msF7vKPiqzeB3NNOox8cueVjz0Qlw6gtOHwnaybBA&A&qdmE5MQEOzXlaM5oXylglk3RlloezH7rqwhodX3lA8Ck6GvnItljtMQWs7BgzSgNKdb9u0KqIOn3CB_ZLuBMn7ii2UIA1BdvfzJNAv5LnLoWsD0rxKs5CGfS5YK8kZ&lEBngvCBlJM5rCua7p04kmxJhV5v7mRKuAFNOH_qvFHF1UjWNyxgIE6zm4ZXXfN1k1ScU_wxwx2chgRMTEkZpx09wVuDmZFX7uA8rHpSj2PhXwKcnycm0wNQw5tYQcXO7R4fDiUegHD1B9WrxH1YbhvNEzdpGA9wAmBuIncVafoMGcOnFUGBtkzAKoHRh7Q5ci963PDltq6gytndGqQTl9Oif0ElA3tYybmyYH4clBiOwNgcALMBpQPusKKCpn2XF4jvsGPRPscRF4M0Xi1o9ptraP_&44ch5HhrvF5YPpvcDKY8t9w9CPD6JMsP5YEYybXl1M0qv6XWWHvbGKayK_wWwgg7t5GD_9r0bfqIywc5g_BCr7mn1VO7Dk4LJbqA4AvkeZT09TV0IUKu51xzw7V_NfedpYlmujGarH52CqZkKmd&mHUWAw_ENiiztV3gaBxo9CD8ppSbNi0ELign_9&kuQfUEsDBBQAAAAIACINKUhqrmiyeAIAAIsFAAAcAAAAZ2l0c3luY2hpc3RhL3dvcmtpbmdfY29weS5weY1UTY&TMBC951eMFq2cim7K7o2VKg6cEDcWiQNCluNMU1PXjmxns1HV&844sTfdBQRV1Hg_PG&83jjq2FkXYMC6dnbw6EB4GOpCzf7eaa2eraCOmNcHHOVeKJNtaY23Gotsa9vmpR_N5BTfqbYoHGormpLCq7y_iK_KotW2Fjrub9EVxfyGbXRUtkPDo0eZtqRcqYX38M26Azk_2m586LsJsrT1T5RhdV8A0NPgDjhXRgXOS496t44nbsRjho15UyZADFcvogT_wl7SiAQKTkveYuBkU1up1ASavTEnoTDG4AsGp&ARIewRhrl&orAbI69gHXTOHrsAO1oKMDiANVjBAyLsQ_j8&WbTqrDv60ra40bs0bjx&e1mkDySmWGKdKS5zaxYFXvqiDjCbUo2yAfawtbAnqTQuhbywOYzqB0YOyk9N54LJamrXIMLjS6ULOkAUQj4jGMqAwuy&yfyOibP_xyG3pkJEy5k9GgaHixPrPHIWtJUyKCsWUMnxjhYa3jiuTBHI2qNzfar6&FS7jck3&_TOv29nNBn9wJGHLGnm2zd0CXasMjm7_0Aao8wKQW57e_Mjsx_5MEi4zJK7vlSVvRCI22DZQqtKoedFhJL9jayen33LkmwO4bYU6LsJlJGhz0t&ZxPM3fnzYdTqnaemyIU2koFKprFowjlsmm7LDP321cSbHNrC00zbZUyO1teffK_n0Y&M8euPbuC6wh7sWeop6tfRm9ypXEYxAH7jqf7Sd_vR3SXl_0VdSdg8tgwuAfmg3CBrdOILj9SzvdSovdTWjeGvTWKsokxkvG83P4&j2Iigs0tsb9QET_lldeIXXmbDvoLUEsBAhQDFAAAAAgAlgGdRym1baOYGgAAf0YAABQAAAAAAAAAAAAAAKSBAAAAAGdpdHN5bmNoaXN0YS9MSUNFTlNFUEsBAhQDFAAAAAgAQAadRzGQt3FhAgAAbgQAABYAAAAAAAAAAAAAAKSByhoAAGdpdHN5bmNoaXN0YS9SRUFETUUubWRQSwECFAMUAAAACACWAZ1HmgB6rxAAAAAOAAAAJgAAAAAAAAAAAAAApIFfHQAAZ2l0c3luY2hpc3RhL2J1aWxkL2dpdHN5bmNoaXN0YV9pZ25vcmVQSwECFAMUAAAACACWAZ1HC8Yq9hYAAAAUAAAAIwAAAAAAAAAAAAAApIGzHQAAZ2l0c3luY2hpc3RhL2J1aWxkL3B5emlwaXN0YV9pZ25vcmVQSwECFAMUAAAACADtBChIg4PeUfoDAAC5DQAAFgAAAAAAAAAAAAAApIEKHgAAZ2l0c3luY2hpc3RhL2NvbmZpZy5weVBLAQIUAxQAAAAIADwNKUgnYyyCdgAAAJYAAAAkAAAAAAAAAAAAAACkgTgiAABnaXRzeW5jaGlzdGEvZXRjL2dpdHN5bmNoaXN0YV9jb25maWdQSwECFAMUAAAACAAiDSlIbxYY9AsDAAAKBwAAKwAAAAAAAAAAAAAApIHwIgAAZ2l0c3luY2hpc3RhL2V0Yy9naXRzeW5jaGlzdGFfY29uZmlnX3NhbXBsZVBLAQIUAxQAAAAIAJYBnUe_Tbr3ZAAAAIQAAAAhAAAAAAAAAAAAAACkgUQmAABnaXRzeW5jaGlzdGEvZXRjL3B5emlwaXN0YV9jb25maWdQSwECFAMUAAAACAB1AidIBcPMv&8BAADOBQAAHAAAAAAAAAAAAAAApIHnJgAAZ2l0c3luY2hpc3RhL2dpdHN5bmNoaXN0YS5weVBLAQIUAxQAAAAIAHUCJ0jCfCKjCQAAAAcAAAAkAAAAAAAAAAAAAACkgSApAABnaXRzeW5jaGlzdGEvbG9nL2dpdHN5bmNoaXN0YV9pZ25vcmVQSwECFAMUAAAACADtBChIa7k8Zo0BAADfAwAAEwAAAAAAAAAAAAAApIFrKQAAZ2l0c3luY2hpc3RhL2xvZy5weVBLAQIUAxQAAAAIACINKUj9_KyDEw4AAAw&AAAUAAAAAAAAAAAAAACkgSkrAABnaXRzeW5jaGlzdGEvc3luYy5weVBLAQIUAxQAAAAIACINKUgbOZ7vVQEAAIQDAAAbAAAAAAAAAAAAAACkgW45AABnaXRzeW5jaGlzdGEvc3luY19jb25maWcucHlQSwECFAMUAAAACACSdChI8AfshtgEAADcEQAAHQAAAAAAAAAAAAAApIH8OgAAZ2l0c3luY2hpc3RhL3N5bmNfc2VsZWN0b3IucHlQSwECFAMUAAAACADtBChI&fQRx30CAADMBwAAHwAAAAAAAAAAAAAApIEPQAAAZ2l0c3luY2hpc3RhL3N5bmNfc2VsZWN0b3IucHl1aVBLAQIUAxQAAAAIAHUCJ0i21zel2wAAALwBAAAUAAAAAAAAAAAAAACkgclCAABnaXRzeW5jaGlzdGEvdGVzdC5weVBLAQIUAxQAAAAIAHUCJ0jf7YmPQQYAAMQWAAAXAAAAAAAAAAAAAACkgdZDAABnaXRzeW5jaGlzdGEvdWlfdXRpbC5weVBLAQIUAxQAAAAIACINKUhqrmiyeAIAAIsFAAAcAAAAAAAAAAAAAACkgUxKAABnaXRzeW5jaGlzdGEvd29ya2luZ19jb3B5LnB5UEsFBgAAAAASABIAOgUAAP5MAABGAEdlbmVyYXRlZCBieSBweXppcGlzdGEucHkgKHNlZSBodHRwczovL2dpdGh1Yi5jb20vbWFyY3VzNjcvcHl6aXBpc3RhKS4=
'''

def main():

  try:  

    print "Decoding base64 encoded ZIP archive into string..."
    binary_zip_string = base64.b64decode(zip_string, '_&')
    binary_zip_input = StringIO.StringIO(binary_zip_string)
  
    print "Opening string as ZIP file..."
    zip_file = zipfile.ZipFile(binary_zip_input, "r")
  
    zip_file.printdir()
    
    print "Extracting ..."
    
    zip_file.extractall()
    
    print "All files successfully extracted into local directory."
  
  except Exception as e:
    
    sys.stderr.write("ERROR '%s' while extracting files!" % str(e))
    
if __name__ == '__main__':
  main()
  
