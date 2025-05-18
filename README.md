# Bansal Solecki Pop index

This is a "better" passport index which takes into account the "desirability" of countries.

Instead of adding 1 for each country the passport grants access to we add $1*h_c$$

$$h_c = \frac{\text{number of countries passport of country $c$ can visit}}{\text{total number of countries}}$$

If many countries are willing to grant visa-free access to citizens of country X, it suggests that country X has positive relations with many nations and is considered "desirable" to visit.

You can read more about this in my blog here - https://prnvbn.github.io/posts/passport-index/

## Interesting results

On comparing this to the widely accepted [Henley Passport Index](https://www.henleyglobal.com/passport-index) here are the most interesting changes:

- The strongest passport is now South Korea! (was #3, now is #1)
- The following countries had a jump of more than 10 upwards

```
 country_name  hp_strength  bsp_strength  bsp_strength_diff
       Kosovo          114            96                 18
     Mongolia          139           126                 13
         Peru           70            58                 12
     Cambodia          163           152                 11
      Vietnam          169           158                 11
      Georgia           89            78                 11
```

## Full output

<details>

<summary>Full output showing the difference in the HP and BSP index scores</summary>

```
                  country_name  hp_strength  bsp_strength  bsp_strength_diff
                        Kosovo          114            96                 18
                      Mongolia          139           126                 13
                          Peru           70            58                 12
                      Cambodia          163           152                 11
                       Vietnam          169           158                 11
                       Georgia           89            78                 11
                       Iceland           36            27                  9
                   Philippines          138           129                  9
                          Cuba          146           137                  9
                 Liechtenstein           38            30                  8
                      Paraguay           67            60                  7
                    Madagascar          152           145                  7
                       Armenia          134           127                  7
                    Tajikistan          158           151                  7
                      Djibouti          177           171                  6
                  Turkmenistan          176           170                  6
          United Arab Emirates           27            21                  6
                         Haiti          162           157                  5
                      Colombia           77            72                  5
            Dominican Republic          124           119                  5
                     Sri Lanka          186           181                  5
                        Norway           16            11                  5
                       Ireland            9             4                  5
                        Bhutan          168           163                  5
                       Uruguay           56            52                  4
                      Suriname          119           115                  4
                    Azerbaijan          128           124                  4
                   Timor-Leste           99            95                  4
                      Thailand          113           109                  4
                         India          154           150                  4
                    Bangladesh          192           188                  4
                          Laos          178           174                  4
         Sao Tome and Principe          145           142                  3
                    Kazakhstan          116           113                  3
                        Tuvalu           83            80                  3
                       Ukraine           64            61                  3
                   El Salvador           73            70                  3
                       Belarus          115           112                  3
                         Egypt          171           168                  3
                        Brazil           47            44                  3
                         Gabon          151           148                  3
                        Jordan          167           165                  2
                       Bolivia          118           116                  2
                          Iran          187           185                  2
                Comoro Islands          164           162                  2
                     Indonesia          122           120                  2
         Palestinian Territory          191           189                  2
                     Venezuela           92            90                  2
                         Nepal          193           191                  2
                   South Korea            3             1                  2
                       Romania           42            40                  2
                        Cyprus           39            37                  2
             Macao (SAR China)           68            66                  2
                   New Zealand           20            18                  2
                  Vatican City           58            56                  2
                   Netherlands           15            13                  2
                    Costa Rica           61            59                  2
                       Austria           14            12                  2
                       Jamaica          105           104                  1
                       Türkiye           94            93                  1
                    Kyrgyzstan          142           141                  1
                        Guinea          155           154                  1
                      Barbados           51            50                  1
                          Fiji          104           103                  1
                       Burundi          174           173                  1
                      Ethiopia          179           178                  1
                      Bulgaria           40            39                  1
                         Italy           10             9                  1
                       Lebanon          183           182                  1
                   South Sudan          184           183                  1
                       Albania           90            89                  1
                        Serbia           72            71                  1
                      Pakistan          196           195                  1
               North Macedonia           80            79                  1
                       Lesotho          120           121                 -1
                       Denmark            4             5                 -1
                        Brunei           50            51                 -1
                United Kingdom           21            22                 -1
                       Andorra           44            45                 -1
                      eSwatini          121           122                 -1
                      Slovenia           33            34                 -1
            Russian Federation           93            94                 -1
                        Monaco           41            42                 -1
                         Japan            2             3                 -1
St. Vincent and the Grenadines           54            55                 -1
                       Moldova           91            92                 -1
                          Oman          110           111                 -1
                          Chad          166           167                 -1
                        Angola          175           176                 -1
                     Nicaragua           84            85                 -1
                       Ecuador          100           101                 -1
                        Zambia          131           132                 -1
                         Yemen          195           196                 -1
                  Saudi Arabia          106           107                 -1
                       Bahrain          107           108                 -1
                     Singapore            1             2                 -1
                       Eritrea          188           190                 -2
                      Portugal           13            15                 -2
                        Poland           22            24                 -2
                         Sudan          185           187                 -2
                          Togo          147           149                 -2
             Congo (Dem. Rep.)          182           184                 -2
                        Greece           18            20                 -2
                       Belgium           12            14                 -2
                         Ghana          133           135                 -2
                    San Marino           45            47                 -2
                      Tanzania          129           131                 -2
        Bosnia and Herzegovina           85            87                 -2
                         Qatar           95            97                 -2
                  South Africa           96            98                 -2
                        Belize           97            99                 -2
                        Kuwait           98           100                 -2
                         Nauru          108           110                 -2
                       Bahamas           52            54                 -2
                      Botswana          111           114                 -3
                         Libya          190           193                 -3
                   North Korea          189           192                 -3
           Trinidad and Tobago           62            65                 -3
                       Vanuatu          103           106                 -3
             Equatorial Guinea          157           160                 -3
                    Mauritania          153           156                 -3
                     St. Lucia           66            69                 -3
                      Slovakia           30            33                 -3
                       Grenada           65            68                 -3
                       Tunisia          135           138                 -3
                    Mozambique          143           146                 -3
                         Benin          136           139                 -3
                       Estonia           28            32                 -4
                        Uganda          130           134                 -4
                      Cameroon          173           177                 -4
                         Kenya          126           130                 -4
                      Maldives          101           105                 -4
                    Micronesia           87            91                 -4
                        Latvia           32            36                 -4
                      Malaysia           37            41                 -4
                      Dominica           69            73                 -4
                     Australia           24            28                 -4
            Cape Verde Islands          132           136                 -4
                     Lithuania           34            38                 -4
                       Nigeria          181           186                 -5
                       Liberia          170           175                 -5
                         Spain            5            10                 -5
                         Tonga           79            84                 -5
           Antigua and Barbuda           59            64                 -5
                         Samoa           78            83                 -5
                       Morocco          123           128                 -5
                       Algeria          159           164                 -5
                       Senegal          148           153                 -5
                    Luxembourg           11            16                 -5
                         Niger          156           161                 -5
                 Guinea-Bissau          161           166                 -5
                  Burkina Faso          149           155                 -6
                       Namibia          117           123                 -6
                         China          112           118                 -6
       Taiwan (Chinese Taipei)           71            77                 -6
                  Sierra Leone          137           143                 -6
                        Rwanda          141           147                 -6
                    The Gambia          127           133                 -6
                    Seychelles           55            62                 -7
                  Congo (Rep.)          172           179                 -7
      Central African Republic          165           172                 -7
                     Mauritius           60            67                 -7
              Papua New Guinea          109           117                 -8
                 Cote d'Ivoire          150           159                 -9
                          Mali          160           169                 -9
Stats on the difference in the HP and BSP index scores:
count    165.000000
mean       0.000000
std        4.590552
min       -9.000000
25%       -3.000000
50%       -1.000000
75%        2.000000
max       18.000000
```

</details>
