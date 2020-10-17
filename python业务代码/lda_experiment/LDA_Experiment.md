
# 1.package lda
关于使用lda这个包训练lda主题模型，http://chrisstrelioff.ws/sandbox/2014/11/13/getting_started_with_latent_dirichlet_allocation_in_python.html
这个链接中的文章写的非常清楚了，下面的代码及说明基本是来自于这个链接中的说明和官方文档。

也部分参考了这个链接
https://blog.csdn.net/Eastmount/article/details/50824215


```python
import numpy as np
import lda
```

## 1.1 载入数据
X是训练集，395个documents，4258个words，组成了vocabulary。其中每个元素代表的都是词频。


```python
X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
X.shape
```




    (395, 4258)




```python
len(vocab)
```




    4258




```python
len(titles)
```




    395




```python
X
```




    array([[1, 0, 1, ..., 0, 0, 0],
           [7, 0, 2, ..., 0, 0, 0],
           [0, 0, 0, ..., 0, 0, 0],
           ...,
           [1, 0, 1, ..., 0, 0, 0],
           [1, 0, 1, ..., 0, 0, 0],
           [1, 0, 1, ..., 0, 0, 0]], dtype=int32)




```python
vocab[0:10]
```




    ('church',
     'pope',
     'years',
     'people',
     'mother',
     'last',
     'told',
     'first',
     'world',
     'year')




```python
titles
```




    ('0 UK: Prince Charles spearheads British royal revolution. LONDON 1996-08-20',
     '1 GERMANY: Historic Dresden church rising from WW2 ashes. DRESDEN, Germany 1996-08-21',
     "2 INDIA: Mother Teresa's condition said still unstable. CALCUTTA 1996-08-23",
     '3 UK: Palace warns British weekly over Charles pictures. LONDON 1996-08-25',
     '4 INDIA: Mother Teresa, slightly stronger, blesses nuns. CALCUTTA 1996-08-25',
     "5 INDIA: Mother Teresa's condition unchanged, thousands pray. CALCUTTA 1996-08-25",
     '6 INDIA: Mother Teresa shows signs of strength, blesses nuns. CALCUTTA 1996-08-26',
     "7 INDIA: Mother Teresa's condition improves, many pray. CALCUTTA, India 1996-08-25",
     '8 INDIA: Mother Teresa improves, nuns pray for "miracle". CALCUTTA 1996-08-26',
     '9 UK: Charles under fire over prospect of Queen Camilla. LONDON 1996-08-26',
     '10 UK: Britain tells Charles to forget Camilla. LONDON 1996-08-27',
     "11 COTE D'IVOIRE: FEATURE - Quiet homecoming for reprieved Ivory Coast maid. ABIDJAN 1996-08-28",
     '12 INDIA: Mother Teresa ("I want to go home") sits and prays. CALCUTTA 1996-08-28',
     '13 INDIA: Mother Teresa nears end of crisis, nuns rejoice. CALCUTTA 1996-08-28',
     '14 UK: Prosaic end for marriage of Charles and Diana. LONDON 1996-08-28',
     '15 UK: No respite for British royals despite divorce. LONDON 1996-08-28',
     "16 UK: Camilla, love of Charles' life, an unlikely queen. LONDON 1996-08-28",
     '17 UK: Diana sets out on new life as single woman. LONDON 1996-08-28',
     '18 USA: O.J. Simpson attacks media, hints at lawsuits. WASHINGTON 1996-08-28',
     '19 USA: U.S. Cardinal Bernardin has one year or less to live. CHICAGO 1996-08-30',
     '20 USA: U.S. Cardinal Bernardin says has terminal cancer. CHICAGO 1996-08-30',
     '21 ROMANIA: German architect wins Bucharest rebuilding prize. BUCHAREST 1996-09-02',
     '22 ARGENTINA: Argentina\'s "Blond Angel" finally quits Navy. BUENOS AIRES, Argentina 1996-09-02',
     '23 UK: Disney lights up Pocahontas resting place. GRAVESEND, England 1996-09-06',
     '24 HUNGARY: POPE LEAVES HUNGARY AFTER DEMANDING TWO-DAY VISIT. BUDAPEST 1996-09-07',
     '25 HUNGARY: Pope says mass in Hungary, health in spotlight. GYOR, Hungary 1996-09-07',
     "26 UK: Prince Charles' love will not wed him, paper says. LONDON 1996-09-09",
     '27 UK: Ex-archbishop calls Princess Diana actress-schemer. LONDON 1996-09-09',
     '28 USA: Politics discussed backstage at Emmys, no airplay. PASADENA, Calif 1996-09-08',
     '29 UK: Diana angered by ex-archbishop\'s "schemer" jibe. LONDON 1996-09-11',
     '30 UK: Queen Elizabeth to hold "royal summit" - report. LONDON 1996-09-10',
     "31 BRAZIL: Nobel Prize winner sides with Brazil's landless. BRASILIA 1996-09-10",
     "32 VATICAN: FEATURE - Papal health in spotlight amid talk of Parkinson's. VATICAN CITY 1996-09-13",
     '33 UK: Cool it with Camilla, Major tells Charles - paper. LONDON 1996-09-14',
     '34 ROMANIA: Romania "royalty" wedding draws business barons. BUCHAREST 1996-09-15',
     '35 UK: British royal family holds meeting on future. LONDON 1996-09-15',
     '36 UK: Scandal-battered British royals debate future role. LONDON 1996-09-16',
     "37 SOUTH AFRICA: It's wonderful I've found Nelson, says new love. JOHANNESBURG 1996-09-17",
     '38 CHILE: Chilean economist Felipe Herrera dies at 74. SANTIAGO 1996-09-18',
     '39 GREECE: Princess Diana joins in funeral on Greek island. LIMNI, Greece 1996-09-18',
     '40 USA: U.S. House of Representatives honors Mother Teresa. WASHINGTON 1996-09-17',
     "41 FRANCE: Jewish-born cardinal is Pope's key man in France. PARIS 1996-09-18",
     "42 VATICAN: Pope's health will figure large on trip to France. VATICAN CITY 1996-09-18",
     '43 PHILIPPINES: FEATURE - Ex-actor eyes Philippine presidency. [CORRECTED 03:43 GMT] MANILA 1996-09-18',
     '44 UK: Runaway bishop had child, Catholic church admits. LONDON 1996-09-19',
     '45 FRANCE: Pope skirts religious controversy in France. TOURS, France 1996-09-19',
     "46 FRANCE: Pope visits western France religious stronghold. SAINTE-ANNE D'AURAY, France 1996-09-20",
     '47 UK: "I still love him" says runaway bishop\'s mistress. LONDON 1996-09-21',
     '48 UK: Church appeals to runaway Scottish bishop. LONDON 1996-09-21',
     "49 SWITZERLAND: Romanian ex-king's daughter marries. LAUSANNE 1996-09-21",
     "50 SWITZERLAND: ROMANIAN EX-KING'S DAUGHTER MARRIES. LAUSANNE 1996-09-21",
     '51 UK: Errant Catholic bishop wants to marry divorcee. LONDON 1996-09-22',
     '52 FRANCE: Pope speaks of death with "a smile"-Cardinal. REIMS, France 1996-09-22',
     '53 USA: Actress Dorothy Lamour dead at 81. LOS ANGELES 1996-09-23',
     '54 USA: South Georgia resort kept Kennedy wedding secret. CUMBERLAND ISLAND, Ga 1996-09-23',
     '55 FRANCE: FEATURE - Bardot tells all - for the love of animals. PARIS 1996-09-24',
     '56 FRANCE: Bardot tells all - for the love of animals. [CORRECTED 09:05 GMT] PARIS 1996-09-24',
     '57 AUSTRALIA: Quiet Buddhist farewell for mercy death Australian. DARWIN, Australia 1996-09-27',
     '58 AUSTRALIA: Australia mercy death man joked until the end. DARWIN, Australia 1996-09-27',
     '59 BELGIUM: Famed Belgian battlefield site makes its mark. WATERLOO, Belgium 1996-09-28',
     "60 REPUBLIC OF IRELAND: Ireland's Cardinal Daly steps down at 79. DUBLIN 1996-10-01",
     '61 CANADA: Former Quebec premier fought for Canadian unity. QUEBEC CITY 1996-10-02',
     '62 GERMANY: Feminist Hite seeks European parliament platform. FRANKFURT 1996-10-04',
     '63 UK: Prince Charles aide out after gaffes over Camilla. LONDON 1996-10-05',
     '64 GERMANY: Vargas Llosa urges sanctions on rights abuses. FRANKFURT 1996-10-06',
     '65 VATICAN: Tired Pope calls for prayers before operation. VATICAN CITY 1996-10-06',
     '66 ITALY: Pope ready for appendix surgery. ROME 1996-10-08',
     '67 FRANCE: FEATURE - "Who\'s Who" sounds requiem for French intellectuals. PARIS 1996-10-07',
     '68 USA: Clinton wishes Pope "speedy recovery". WASHINGTON 1996-10-08',
     '69 ITALY: "Textbook" papal appendix surgery excludes tumour. [CORRECTED 16:45 GMT] ROME 1996-10-08',
     '70 ITALY: Pope gets clean bill of health after appendectomy. ROME 1996-10-09',
     '71 UK: Runaway UK bishop to marry, apologises to church. KENDAL, England 1996-10-08',
     "72 ITALY: Pope's surgery a success, doctors say no tumour. ROME 1996-10-08",
     '73 UK: Runaway Scottish bishop to marry lover. GLASGOW, Scotland 1996-10-08',
     '74 ITALY: Pope has appendix removed, no problems. ROME 1996-10-08',
     '75 ITALY: Tranquil Pope has appendix surgery. ROME 1996-10-08',
     "76 ITALY: Pope's operation starts - hospital sources. ROME 1996-10-08",
     '77 SOUTH KOREA: "King of Pop" Michael Jackson arrives in Seoul. SEOUL 1996-10-09',
     '78 SOUTH KOREA: Jackson takes to stage in Seoul despite protests. SEOUL 1996-10-11',
     '79 INDONESIA: Nobel peace awards put East Timor in spotlight. JAKARTA 1996-10-11',
     '80 NORWAY: Nobel peace award wins praise outside indonesia. OSLO 1996-10-11',
     "81 VATICAN: Bishop's Nobel prize sweet satisfaction for Pope. VATICAN CITY 1996-10-11",
     '82 NORWAY: Winners of Nobel Peace Prize since 1970. OSLO 1996-10-11',
     '83 SOUTH AFRICA: FEATURE - Germans cling to little oasis in rural South Africa. HERMANNSBURG, South Africa 1996-10-13',
     '84 GERMANY: German publisher of Stern magazine dies. HAMBURG, Germany 1996-10-13',
     '85 ITALY: Joking Pope appears in public after surgery. ROME 1996-10-13',
     '86 INDONESIA: Nobel laureate invited to gathering for Suharto. JAKARTA 1996-10-14',
     '87 VATICAN: After appendectomy, Papal trembling in spotlight. VATICAN CITY 1996-10-14',
     '88 USA: Material Girl Madonna becomes a mother. LOS ANGELES 1996-10-14',
     '89 USA: Madonna as mother - the next chapter. LOS ANGELES 1996-10-14',
     '90 REPUBLIC OF IRELAND: Irish aid agency pulls out of concert over singer. DUBLIN 1996-10-15',
     '91 UK: British writer seeks reward on Nazi gold-raid book. LONDON 1996-10-18',
     "92 UK: Mahatma Ghandi's letters go on sale in London. LONDON 1996-10-21",
     "93 UK: Mahatma Gandhi's letters go on sale in London. LONDON 1996-10-21",
     '94 USA: FEATURE-Haitian voodoo - more than dolls and zombies. MIAMI 1996-10-22',
     '95 VATICAN: Pope to celebrate public mass on Sunday. VATICAN CITY 1996-10-22',
     '96 VATICAN: Pope greets pilgrims, resumes full duties Sunday. VATICAN CITY 1996-10-23',
     "97 SPAIN: Spanish bishops attack minister's lavish wedding. MADRID 1996-10-23",
     '98 INDIA: Former Gandhi aide has second thoughts on auction. MADRAS, India 1996-10-24',
     '99 UK: ENGLISH PASTOR DEFENDS MEMORIAL SERVICE FOR MONKEY. LONDON 1996-10-25',
     '100 VATICAN: Pope gradually resumes activity after operation. VATICAN CITY 1996-10-27',
     '101 RUSSIA: Russia presents archives to U.S. Holocaust museum. MOSCOW 1996-10-28',
     '102 USA: Municipal industry mourns James Augenthaler. NEW YORK 1996-10-28',
     '103 UK: U.S. actor berates archbishop over smacking. LONDON 1996-10-28',
     '104 USA: Author who denied Japanese-Americans interned dies. LOS ANGELES 1996-10-29',
     '105 VATICAN: Pope to publish brief memoirs. VATICAN CITY 1996-10-31',
     '106 VATICAN: Pope marks 50 years as priest, announces memoirs. VATICAN CITY 1996-11-01',
     '107 VATICAN: FEATURE - Pope marks 50th anniversary of priesthood. VATICAN CITY 1996-11-01',
     '108 ROMANIA: Romanians enjoy colourful choice of candidates. BUCHAREST 1996-11-03',
     '109 RUSSIA: Veil of secrecy thickens as Yeltsin surgery nears. MOSCOW 1996-11-04',
     '110 RUSSIA: Yeltsin in good form as heart operation nears. MOSCOW 1996-11-04',
     '111 RUSSIA: Yeltsin op looks imminent, security tightened. MOSCOW 1996-11-05',
     '112 RUSSIA: FEATURE - Provincial museum fights to stay open in Russia. KOSTROMA, Russia 1996-11-04',
     '113 ARGENTINA: FEATURE - Erstwhile angel Cavallo bedevils government. BUENOS AIRES 1996-11-04',
     '114 RUSSIA: YELTSIN COMES THROUGH SEVEN-HOUR HEART OPERATION. MOSCOW 1996-11-05',
     '115 RUSSIA: Russia on edge as Yeltsin surgery goes to plan. MOSCOW 1996-11-05',
     '116 RUSSIA: Yeltsin comes through seven-hour heart operation. MOSCOW 1996-11-05',
     "117 ITALY: Real-life Don Camillo won't toll bells for red. ROME 1996-11-06",
     '118 VATICAN: Pope celebrates priesthood, to resume all activity. VATICAN CITY 1996-11-10',
     "119 USA: Chicago's Cardinal Bernardin reported near death. CHICAGO 1996-11-13",
     '120 USA: Church, lay leaders mourn Chicago cardinal. CHICAGO 1996-11-14',
     "121 USA: Bishops recall Bernardin's humble leadership. WASHINGTON 1996-11-14",
     '122 USA: Cardinal led Chicago archdiocese for 14 years. CHICAGO 1996-11-14',
     "123 USA: Chicago's Cardinal Bernardin dead at age 68. CHICAGO 1996-11-14",
     '124 VATICAN: Pope saddened over Bernardin death. VATICAN CITY 1996-11-14',
     '125 CROATIA: Croatian doctor says Tudjman "feeling excellent". ZAGREB 1996-11-16',
     '126 INDONESIA: Norway issues Timorese Nobel laureate a visa. JAKARTA 1996-11-17',
     '127 INDIA: Mother Teresa becomes honorary American citizen. NEW DELHI 1996-11-16',
     '128 VATICAN: Pope warms up for Castro by meeting Gorbachev. VATICAN CITY 1996-11-18',
     '129 USA: Final services for Cardinal Bernardin of Chicago. CHICAGO 1996-11-20',
     '130 UK: India saves Gandhi papers from jaws of commerce. LONDON 1996-11-22',
     "131 USA: Simpson's life story defies imagination. SANTA MONICA, Calif. 1996-11-22",
     '132 INDIA: Mother Teresa "comfortable" after heart failure. CALCUTTA 1996-11-22',
     '133 INDIA: Mother Teresa in hospital with heart problem. CALCUTTA 1996-11-22',
     '134 FRANCE: France pays tribute to writer Malraux on Saturday. PARIS 1996-11-22',
     '135 USA: S. Carolina Klan museum claims to teach history. LAURENS, S.C. 1996-11-24',
     '136 USA: Ex-hostage Waite still keeps symbolic ticket. NEW YORK 1996-11-26',
     "137 UK: Cluedo's final mystery solved at inventor's grave. LONDON 1996-11-27",
     "138 MOLDOVA: Moldova's new leader has Moscow past, western goals. CHISINAU 1996-12-02",
     '139 VATICAN: Belgian cardinal Hamer dies. VATICAN CITY 1996-12-02',
     '140 UK: Papers show Duke of Windsor was royal loose cannon. LONDON 1996-12-03',
     '141 FRANCE: Acclaimed French historian Georges Duby dies at 77. PARIS 1996-12-03',
     '142 CENTRAL AFRICAN REPUBLIC: State burial for African emperor Bokassa cancelled. BANGUI 1996-12-04',
     '143 INDIA: Mother Teresa seeks foster homes for 4,000 children. CALCUTTA 1996-12-05',
     '144 USA: Abortion foe Salvi buried, victim attends funeral. IPSWICH, Mass 1996-12-04',
     '145 ITALY: Nobel laureate Belo says peace will be his message. ROME 1996-12-06',
     '146 VIETNAM: Hanoi declares dissident temple a national site. HANOI 1996-12-06',
     '147 GREECE: SALONIKA TO SHOW OFF BYZANTINE LEGACY IN 1997. SALONIKA, Greece 1996-12-08',
     '148 GREECE: SALONIKA TO SHOW OFF BYZANTINE LEGACY IN 1997. SALONIKA, Greece 1996-12-09',
     '149 RUSSIA: Cash-strapped Kremlin to start charging visitors. MOSCOW 1996-12-10',
     '150 VATICAN: Ageing Pope to skip Christmas Day mass this year. VATICAN CITY 1996-12-10',
     '151 NORWAY: East Timor activist shares peace prize. OSLO 1996-12-10',
     "152 UK: FEATURE - Duke's reputation sinks 60 years after abdication. LONDON 1996-12-11",
     "153 SOUTH AFRICA: S.Africa's Boesak charged with theft of aid funds. CAPE TOWN 1996-12-13",
     "154 ITALY: Italy's Dossetti, political figure, dies. BOLOGNA, Italy 1996-12-15",
     '155 GREECE: FEATURE - Salonika to show off Byzantine legacy in 1997. SALONIKA, Greece 1996-12-15',
     '156 NETHERLANDS: Hermitage treasures on show in Amsterdam. AMSTERDAM 1996-12-16',
     '157 RUSSIA: Russian Orthodox leader taken to hospital. MOSCOW 1996-12-18',
     '158 FRANCE: Bardot denies racism charge in Paris court. PARIS 1996-12-19',
     '159 FRANCE: Paris bids emotional farewell to Mastroianni. PARIS 1996-12-20',
     '160 ITALY: Italy says "Ciao Marcello," thanks for sweet life. ROME 1996-12-20',
     '161 PERU: Peru rebel chief is angry, violent revolutionary. LIMA 1996-12-22',
     '162 CUBA: Santa Claus skips Cuba, at least officially. HAVANA 1996-12-23',
     '163 ISRAEL: Israel takes shine off Christmas in Bethlehem. BETHLEHEM, West Bank 1996-12-23',
     '164 RUSSIA: FEATURE - Moscow to celebrate 850th birthday in grand style. MOSCOW 1996-12-25',
     '165 UK: Fred West film plan angers British MPs, relatives. LONDON 1996-12-31',
     '166 INDIA: Israel president shrugs off illness. NEW DELHI 1996-12-31',
     '167 UK: Britain to review law after Fred West film plan. LONDON 1997-01-01',
     '168 UK: Britain to review law after Fred West film plan. LONDON 1997-01-01',
     '169 USA: Mother Teresa "miracle" bun takes to the Internet. NASHVILLE, Tenn. 1997-01-03',
     "170 SWEDEN: Sweden's honourable Prince Bertil dies, aged 84. STOCKHOLM 1997-01-05",
     "171 SWEDEN: Sweden's Prince Bertil dies. STOCKHOLM 1997-01-05",
     "172 RUSSIA: Kremlin slams report on return of Tsar's heir. MOSCOW 1997-01-06",
     '173 RUSSIA: Yeltsin spends Russian Christmas in bed with cold. MOSCOW 1997-01-07',
     '174 SOUTH KOREA: Under plastic awning, veteran newsman leads strikes. SEOUL 1997-01-07',
     '175 RUSSIA: FEATURE - Russian historian seeks real Stalin behind myth. MOSCOW 1997-01-09',
     '176 GERMANY: Hollywood stars blast Germany over Scientologists. BONN 1997-01-09',
     "177 Germany: Kohl dismisses Hollywood stars' rebuke of Germany. BONN 1997-01-09",
     '178 UK: Buckingham Palace to campaign for Charles as king. LONDON 1997-01-09',
     "179 CANADA: FEATURE-Canada's Ben Heppner -- the Fourth Tenor?. OTTAWA 1997-01-10",
     "180 GERMANY: Germany rebuffs stars' accusations over Scientology. BONN 1997-01-10",
     "181 RUSSIA: FEATURE - Russian artists say forging evidence is kids' stuff. MOSCOW 1997-01-12",
     '182 USA: Houston moves to rein in topless nightclubs. HOUSTON 1997-01-12',
     '183 SWEDEN: Sweden, European royalty mourn Prince Bertil. STOCKHOLM 1997-01-13',
     '184 GERMANY: German Jewish leader slams Scientology letter. FRANKFURT 1997-01-13',
     '185 PHILIPPINES: FEATURE - Festivals bring buried Philippine towns back to life. ANGELES CITY, Philippines 1997-01-13',
     '186 SWEDEN: European royalty join Sweden to mourn Prince Bertil. STOCKHOLM 1997-01-13',
     '187 AUSTRALIA: RTRS-TIMELINES-Today in History - Jan 15.',
     '188 DENMARK: Danish queen mourns, marks 25 years as monarch. COPENHAGEN 1997-01-14',
     "189 SOUTH AFRICA: S.Africa's moral conscience, Tutu, battles cancer. JOHANNESBURG 1997-01-17",
     '190 USA: Debate over King legacy dampens Atlanta festivities. ATLANTA 1997-01-19',
     '191 USA: Church marks legacy of Martin Luther King Jr.. ATLANTA 1997-01-20',
     '192 USA: U.S. Sen. Tsongas to be buried on Thursday. LOWELL, Mass 1997-01-19',
     '193 USA: Friends line up to pay respects to Tsongas. LOWELL, Mass. 1997-01-21',
     '194 USA: John Phillips dies, ex-First Boston muni official. NEW YORK 1997-01-22',
     "195 FRANCE: France's Bardot cleared of racist slur. PARIS 1997-01-23",
     "196 LIBERIA: Liberia's Taylor remarries, offers toast for peace. GBANGA, Liberia 1997-01-28",
     '197 TAIWAN: Taiwan president soul-searches with Hollywood hunk. TAIPEI 1997-01-29',
     '198 COLOMBIA: Gays beat Church ban, parade in Colombian carnival. BOGOTA 1997-02-02',
     '199 FRANCE: U.S. ambassador to France has brain haemorrhage. PARIS 1997-02-04',
     '200 GERMANY: Berlin festival quells Scientology boycott fears. BERLIN 1997-02-04',
     '201 USA: U.S. envoy to France seriously ill. WASHINGTON 1997-02-03',
     '202 USA: U.S. envoy to France said to be near death. WASHINGTON 1997-02-03',
     '203 FRANCE: U.S. Paris envoy Harriman in serious condition. PARIS 1997-02-04',
     '204 FRANCE: U.S. ambassador to France has brain haemorrhage. PARIS 1997-02-04',
     '205 FRANCE: U.S. ambassador to France ill in hospital. PARIS 1997-02-04',
     '206 USA: Pamela Harriman eulogized by Clinton, Democrats. WASHINGTON 1997-02-05',
     '207 USA: Clinton, Democrats laud Pamela Harriman. WASHINGTON 1997-02-05',
     '208 FRANCE: U.S. envoy Pamela Harriman dies in Paris. PARIS 1997-02-05',
     "209 FRANCE: Pamela Harriman's life a mix of wealth and power. PARIS 1997-02-05",
     '210 USA: Clinton lauds Harriman as gifted public servant. WASHINGTON 1997-02-05',
     "211 USA: O.J. Simpson's incredible reversal of fortune. SANTA MONICA, Calif. 1997-02-04",
     '212 FRANCE: U.S. ambassador to Paris Harriman dead at 76. PARIS 1997-02-05',
     '213 FRANCE: Pamela Harriman, U.S. envoy to France, dead at 76. PARIS 1997-02-05',
     '214 FRANCE: U.S. ambassador to France condition still serious. PARIS 1997-02-05',
     '215 FRANCE: Chirac to honour late U.S. envoy Pamela Harriman. PARIS 1997-02-06',
     '216 USA: FEATURE - Marsalis conjures soul from slavery. NEW YORK 1997-02-06',
     '217 UK: Oasis singer Liam Gallagher set to marry next week. LONDON 1997-02-06',
     "218 USA: Harriman's body returned to Washington. WASHINGTON 1997-02-08",
     '219 SWITZERLAND: FEATURE - Troubleshooting Swiss diplomat keeps low profile. BERNE 1997-02-12',
     '220 USA: Clinton recalls Harriman as elegant, indomitable. WASHINGTON 1997-02-13',
     '221 USA: Funeral for baby allegedly killed by British nanny. BROOKLINE, Mass. 1997-02-12',
     '222 VATICAN: Historian of Vatican policy towards Nazis dies. VATICAN CITY 1997-02-14',
     '223 UK: UK watchdog halts ads over epileptic seizure risk. LONDON 1997-02-14',
     "224 PHILIPPINES: Air crash follows bishop's funeral in Philippines. JOLO, Philippines 1997-02-14",
     '225 HONG KONG: China, Taiwan, HK stocks rocked by Deng worries. HONG KONG 1997-02-18',
     '226 UK: Albright looks back to war years on London visit. LONDON 1997-02-19',
     '227 USA: Harriman son, estranged wife inherit - report. WASHINGTON 1997-02-18',
     '228 FRANCE: French judges refuse to ban "Larry Flynt" posters. PARIS 1997-02-20',
     "229 GERMANY: Bavarians outraged at exhibition on Hitler's army. MUNICH, Germany 1997-02-20",
     '230 SWITZERLAND: Swiss bishops blast Larry Flynt film poster. ZURICH 1997-02-21',
     '231 ROMANIA: Romania king, citizenship restored, to visit home. BUCHAREST 1996-02-24',
     '232 CHINA: China Catholics pray for Deng as church silent. BEIJING 1997-02-23',
     '233 ROMANIA: Romania flashy "Gypsy King" dies of heart attack. BUCHAREST 1997-02-24',
     '234 USA: Rev. Benjamin Chavis joins Farrakhan group. CHICAGO 1997-02-24',
     '235 INDIA: Mother Teresa succession vote soon, order says. CALCUTTA, India 1997-02-24',
     '236 INDIA: Mother Teresa succession vote imminent, order says. CALCUTTA, India 1997-02-24',
     '237 GERMANY: "English Patient" favourite for Berlin Golden Bear. BERLIN 1997-02-24',
     '238 FRANCE: Berlin-winner Forman drops Larry Flynt poster. PARIS 1997-02-24',
     "239 GERMANY: Bavarians protest against exhibit on Hitler's army. MUNICH, Germany 1997-01-24",
     '240 GERMANY: "English Patient" tipped for Berlin festival prize. BERLIN 1997-02-24',
     '241 ROMANIA: Romanians honour memory of Gypsy King. SIBIU, Romania 1997-02-26',
     '242 ROMANIA: Romania to use King as envoy to boost NATO chances. BUCHAREST 1997-02-26',
     '243 ITALY: Sicily archbishop on trial for corruption, EU fraud. PALERMO, Sicily 1997-02-26',
     "244 VATICAN: St Peter's in Rome to get facelift for 2000. VATICAN CITY 1997-02-27",
     "245 ROMANIA: Romania's exiled king backs reforms. BUCHAREST 1997-03-01",
     '246 ROMANIA: Small crowds greet Romanian king, patriarch. BUCHAREST 1997-03-02',
     '247 USA: Forbes seeks to shape U.S. agenda, could run again. NEW YORK 1997-03-04',
     '248 INDIA: Mother Teresa successor vote soon - church official. CALCUTTA 1997-03-04',
     '249 POLAND: Polish bishops condemn Larry Flynt film poster. WARSAW 1997-03-05',
     '250 USA: Ex-president Reagan, wife mark 45th anniversary. LOS ANGELES 1997-03-04',
     '251 BULGARIA: Bulgarian patriarch vows to stay on despite ruling. SOFIA 1997-03-06',
     "252 INDIA: Nuns to elect Mother Teresa's successor any day. CALCUTTA 1997-03-06",
     '253 UK: UK Cardinal offers cash help to women not to abort. GLASGOW, Scotland 1997-03-09',
     "254 UK: Charles and Diana reunited for son's confirmation. LONDON 1997-03-09",
     "255 INDIA: Mother Teresa's order grappling with succession. CALCUTTA, India 1997-03-09",
     "256 RUSSIA: FEATURE - Russians still squabbling over tsar's bones. YEKATERINBURG, Russia 1997-03-10",
     "257 USA: Pamela Harriman's estate to be auctioned off. NEW YORK 1997-03-11",
     '258 USA: FEATURE-Grammy Winner Brecker owes it all to Philadelphia. PHILADELPHIA 1997-03-11',
     '259 INDIA: Hindu Brahmin convert to succeed Mother Teresa. CALCUTTA, India 1997-03-13',
     "260 INDIA: Shy nun emerges from Mother Teresa's shadow. CALCUTTA, India 1997-03-13",
     "261 GERMANY: German home of 'lost Gospel' may hold other finds. BERLIN 1997-03-13",
     '262 SPAIN: FEATURE - Spanish fiestas stir animal groups into fury. MANGANESES DE LA POLVOROSA, Spain 1997-03-13',
     "263 INDIA: Mother Teresa's successor faces bumpy start. CALCUTTA, India 1997-03-16",
     '264 SLOVAKIA: SLOVAK STUDENTS PRESS FOR MINISTER TO QUIT. BRATISLAVA 1997-03-17',
     '265 JAMAICA: Former Jamaica prime minister Manley laid to rest. KINGSTON, Jamaica 1997-03-16',
     '266 UK: FEATURE-Maverick Leigh strikes blow for independent film makers. LONDON 1997-03-17',
     '267 USA: Fans swarm New York procession for slain rapper. NEW YORK 1997-03-18',
     '268 USA: Hundreds swarm New York motorcade for slain rapper. NEW YORK 1997-03-18',
     '269 USA: FEATURE - John Tesh - music is entertainment tonight. LOS ANGELES 1997-03-18',
     "270 UK: Thatcher's archive to go to Churchill College. LONDON 1997-03-18",
     '271 EGYPT: Egypt moves ahead with church restoration project. CAIRO 1997-03-18',
     '272 PHILIPPINES: Ramos says N.Korean defector in Philppines for short time. MANILA 1997-03-19',
     '273 UK: Archbishop of Canterbury speaks of retiring. LONDON 1997-03-20',
     '274 ZIMBABWE: Mrs Clinton sees Zimbabwe efforts to help people. HARARE, Zimbabwe 1997-03-22',
     '275 ITALY: Dutch-Flemish show goes to roots of modern art. VENICE, Italy 1997-03-23',
     '276 USA: Clinton adjusts to slower-paced life. WASHINGTON 1997-03-25',
     '277 RUSSIA: Lenin niece opposes re-burial of Communist leader. MOSCOW 1997-03-26',
     "278 INDONESIA: Seventeen detained after riot on Indonesia's Java. JAKARTA 1997-03-27",
     '279 VENEZUELA: FEATURE-Andean hermit acrobat wins artist fame. SAN RAFAEL DE MUCUCHIES, Venezuela 1997-04-01',
     '280 VATICAN: FEATURE - Pope marks 19th Easter season looking tired, frail. VATICAN CITY 1997-04-01',
     "281 PORTUGAL: FEATURE - Portugal's Cinderella city gets its reward.",
     '282 FRANCE: Christian Dior denies rupture with actress Beart. PARIS 1997-04-03',
     '283 SPAIN: Spanish princess to wed handball player - reports. MADRID 1997-04-03',
     '284 UK: Defiant Princess Anne to return for Grand National. LIVERPOOL, England 1997-04-07',
     '285 USA: Writer Patricia Cornwell admits lesbian affair. [CORRECTED 21:20 GMT]. NEW YORK 1997-04-08',
     "286 USA: Joe Kennedy's ex-wife to appeal annulment - report. BOSTON 1997-04-08",
     '287 USA: Ex-wife of US Sen. Kerry fights annulment - report. BOSTON 1997-04-10',
     '288 RUSSIA: Top Russian official meets royal relative. MOSCOW 1997-04-12',
     '289 USA: Farrakhan blames Catholics Church for hate crimes. [CORRECTED 21:48 GMT] WASHINGTON 1997-04-13',
     "290 AUSTRALIA: RTRS-Australia's Colston released from hospital. BRISBANE 1996-04-17",
     '291 UK: FEATURE - Britain hosts major Thomas Becket exhibition. CANTERBURY, England 1997-04-20',
     '292 USA: Brooke Shields and Andre Agassi marry. MONTEREY, Calif. 1997-04-19',
     "293 UK: China's HK General perfect choice, says tutor. LONDON 1997-04-22",
     '294 USA: U.S. Christian Coalition leader to step down. [CORRECTED 18:19 GMT] WASHINGTON 1997-04-23',
     '295 USA: Ralph Reed steps down from U.S. Christian Coalition. WASHINGTON 1997-04-23',
     '296 EGYPT: U.S. pilot heads to Asia on Earhart tribute trip. LUXOR, Egypt 1997-04-24',
     '297 USA: Alabama judge wins Kennedy "Courage" award. BOSTON 1997-04-24',
     '298 PHILIPPINES: Philippines buries Marcos predecessor Macapagal. MANILA 1997-04-27',
     "299 USA: 'Ellen' comes out, gays across U.S. celebrate. MIAMI 1997-05-01",
     "300 USA: 'Ellen' comes out, gays across U.S. celebrate. MIAMI 1997-04-30",
     '301 UK: Worldwide Advertising & Media Digest - May 2.',
     '302 UK: Ex-wife of Yorkshire Ripper weds again in Britain. LONDON 1997-05-03',
     '303 NEW ZEALAND: Former NZ Social Credit leader Bruce Beetham dies.',
     '304 ITALY: Italy unveils plan to protect art treasures. ROME 1997-05-03',
     '305 UK: Eurosceptic Redwood bids to lead UK Conservatives. LONDON 1997-05-06',
     "306 GERMANY: Germany's Herzog urges Europeans to back unity. AACHEN, Germany 1997-05-08",
     '307 USA: American civil rights leader to be buried in Harlem. NEW YORK 1997-05-08',
     '308 USA: Kempton honored by New York writers, mayor. NEW YORK 1997-05-08',
     '309 VATICAN: Glamorous ex-model swaps catwalk for convent. VATICAN CITY 1997-05-09',
     '310 RUSSIA: Russian parliament votes no changes to Red Square. MOSCOW 1997-05-14',
     '311 AUSTRIA: FEATURE - "Sound of Music" makes Austrian cash tills ring. SALZBURG, Austria 1997-05-16',
     '312 AUSTRALIA: TIMELINES-Today in History - May 19.',
     '313 ITALY: Pope, on birthday, says wants to live to 100. ROME 1997-05-18',
     "314 USA: Pamela Harriman's estate goes on sale. [CORRECTED 22:43 GMT] NEW YORK 1997-05-19",
     '315 USA: Stallone married in London, publicist confirms. LOS ANGELES 1997-05-19',
     '316 UK: Germans ran systematic wartime plunder campaign. LONDON 1997-05-19',
     '317 USA: Harriman auction continues to bring high prices. NEW YORK 1997-05-20',
     '318 MEXICO: Mexico bids awkward farewell to controversial cleric. MEXICO CITY 1997-05-21',
     '319 USA: Notebook contains early Lennon-McCartney tunes. NEW YORK 1997-05-21',
     '320 USA: Harriman auction continues to bring high prices. NEW YORK 1997-05-20',
     '321 ITALY: Healthy looking Mother Teresa initiates new nuns. ROME 1997-05-23',
     '322 USA: Mother Teresa in New York to initiate new nuns. NEW YORK 1997-05-26',
     '323 USA: Leona Helmsley makes $1 million donation. NEW YORK 1997-05-28',
     '324 USA: Alabama judge accepts Kennedy "Courage" award. BOSTON 1997-05-29',
     '325 RUSSIA: Would-be Russian tsar to return for family ceremony. MOSCOW 1997-05-30',
     '326 POLAND: Pope in Poland tries to allay health concerns. WROCLAW, Poland 1996-06-02',
     '327 UK: Britain plans glittering royal golden wedding. LONDON 1997-06-04',
     '328 FRANCE: Vaillant gets loyalty reward in French cabinet post. PARIS 1997-06-04',
     '329 POLAND: POPE TAKES HELICOPTER TRIP ON REST DAY. ZAKOPANE, Poland 1997-06-05',
     '330 POLAND: Pope takes helicopter trip over beloved mountains. ZAKOPANE, Poland 1997-06-05',
     '331 POLAND: Pope rests at halfway mark as Poles mull message. ZAKOPANE, Poland 1997-06-05',
     '332 POLAND: Pope has moving reunion with with old schoolmates. ZAKOPANE, Poland 1997-06-06',
     '333 UK: Oasis songwriter Noel Gallagher weds in Las Vegas. LONDON 1997-06-07',
     '334 POLAND: Pope gives thanks for surviving assassination bid. ZAKOPANE, Poland 1997-06-07',
     '335 POLAND: Pope emotionally recalls assassination attempt. ZAKOPANE, Poland 1997-06-07',
     "336 POLAND: Pope to spend few moments at parents' grave. KRAKOW, Poland 1996-06-09",
     "337 POLAND: Pope spends moments of silence at parents' grave. KRAKOW, Poland 1997-06-09",
     '338 POLAND: Poles flock to big mass on last day of Papal visit. KROSNO, Poland 1997-06-10',
     "339 ITALY: Mussolini descendants gather for son's funeral. ROME 1997-06-14",
     '340 ISRAEL: Sinead quits Jerusalem concert after death threats. JERUSALEM 1997-06-16',
     '341 USA: U.S. church boycotts "Gay friendly" Disney. DALLAS 1997-06-18',
     "342 RUSSIA: Russia's Patriarch urges caution on Lenin removal. MOSCOW 1997-06-19",
     '343 GERMANY: Fragments of rare Gutenberg bible found in Germany. BONN 1997-06-20',
     "344 UK: UK ex-minister quits as Queen's adviser - reports. LONDON 1997-06-25",
     '345 GERMANY: Boris Becker threatens Scientology over Internet. BONN 1997-06-27',
     "346 CHINA: China's top Catholic church official dies at 80. BEIJING 1997-06-28",
     '347 UK: Westminster Abbey to charge entry fee - paper. LONDON 1997-06-29',
     '348 UK: Freemasons launch magazine to improve image. LONDON 1997-07-01',
     '349 UK: FEATURE-Orange and Green, the colours of N.Ireland conflict. BELFAST 1997-07-02',
     '350 COLOMBIA: Colombia recovers church art worth $1.5 million. BOGOTA 1997-07-03',
     "351 UK: Rare show of sympathy for UK's royal mistress. LONDON 1997-07-07",
     '352 USA: Hollywood bids farewell to actor Jimmy Stewart. BEVERLY HILLS, Calif. 1997-07-07',
     '353 ITALY: Pope begins private mountain retreat in Italy Alps. INTROD, Italy 1997-07-09',
     '354 UK: FEATURE - UK royals try to relaunch after decade "horribilis". LONDON 1997-07-10',
     '355 USA: Black church leader denies affair. ST. PETERSBURG, Fla. 1997-07-11',
     '356 ALBANIA: FEATURE - Albania violence threatens treasured ancient city. BUTRINT, Albania 1997-07-13',
     '357 ITALY: Jovial Pope seems invigorated by mountain break. LES COMBES, Italy 1997-07-13',
     "358 UK: Churchill's World War One letters up for auction. LONDON 1997-07-16",
     '359 UK: Prince Charles holds 50th bash for lover Camilla. LONDON 1997-07-16',
     '360 GERMANY: Russian minister criticises Bonn on art booty. BONN 1997-07-16',
     '361 UK: Churchill letters sell for three times estimate. LONDON 1997-07-17',
     '362 USA: Miami police probe new killing, Versace cremated. MIAMI 1997-07-17',
     '363 USA: Versace ashes to be flown to Italy Thursday. MIAMI 1997-07-17',
     '364 ISRAEL: FEATURE - Despite Vanunu, no nuclear debate in Israel. JERUSALEM 1997-07-17',
     '365 USA: Miami Beach bids farewell to Versace. MIAMI BEACH, Fla. 1997-07-18',
     '366 ITALY: Lakeside villa was hideaway for glamorous Versace. MOLTRASIO, Italy 1997-07-18',
     '367 USA: Miami Beach bids farewell to Versace. MIAMI BEACH, Fla. 1997-07-18',
     "368 USA: Clinton will speak at Arkansas friend's funeral. HARRISON, Ark 1997-07-18",
     '369 USA: Versace service set; new murder seen as unrelated. MIAMI BEACH 1997-07-18',
     '370 UK: Camilla steps out of shadows as royal lover. LONDON 1997-07-19',
     '371 INDIA: Mother Teresa returns, pleased with foreign trip. NEW DELHI 1997-07-20',
     '372 VIETNAM: Senior Vietnam Buddhist dies. HANOI 1997-07-21',
     '373 RUSSIA: Yeltsin revels in good health, backs new reforms. MOSCOW 1997-07-23',
     '374 PHILIPPINES: Aunt calls Versace killer "nice, quiet boy". BALIUAG, Philippines 1997-07-24',
     '375 VIETNAM: Thousands mourn death of top Vietnam Buddhist. HO CHI MINH CITY, Vietnam 1997-07-25',
     "376 UK: UK's Blair says Charles can wed Camilla - report. LONDON 1997-07-27",
     "377 UK: UK's Blair dismisses Charles and Camilla reports. LONDON 1997-07-28",
     "378 USA: Clinton delivers eulogy at Brennan's funeral. WASHINGTON 1997-07-29",
     '379 USA: California memorial service held for Andrew Cunanan. SAN DIEGO 1997-07-30',
     "380 CROATIA: Croatia's Tudjman sworn in for second 5-year term. ZAGREB 1997-08-05",
     '381 USA: Former FBI Director Clarence Kelley dies at 85. KANSAS CITY, Mo. 1997-08-05',
     '382 UK: Most Britons oppose idea of "Queen Camilla"-poll. LONDON 1997-08-06',
     '383 USA: Clarence Kelley, former FBI director, dies at 85. KANSAS CITY, Mo 1997-08-05',
     '384 UK: Britain\'s "top people" back Charles marrying - poll. LONDON 1997-08-06',
     "385 UK: Scotland kicks off world's biggest arts festival. EDINBURGH 1997-08-10",
     '386 UK: Fringe chases audiences in Edinburgh festival month. EDINBURGH 1996-08-12',
     '387 USA: Even in death, Elvis lives. LOS ANGELES 1997-08-11',
     '388 USA: EVEN IN DEATH, ELVIS LIVES. LOS ANGELES 1997-08-11',
     '389 USA: EVEN IN DEATH, ELVIS LIVES. LOS ANGELES 1997-08-11',
     '390 CANADA: FEATURE - French-speaking Quebec celebrates Irish heritage. QUEBEC CITY 1997-08-14',
     '391 BULGARIA: FEATURE - Bulgarian opera stars are enduring export. SOFIA 1997-08-15',
     '392 USA: Fans end Elvis Presley fete with concert. MEMPHIS, Tenn 1997-08-16',
     '393 UK: Volcano buries studio where rock legends recorded. LONDON 1997-08-18',
     '394 USA: Joseph Vostal, ex-Kidder muni banker, dead at 88. NEW YORK 1997-08-18')



## 1.2 训练LDA模型


```python
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
```


```python
model.fit(X)  # model.fit_transform(X) is also available
```

    INFO:lda:n_documents: 395
    INFO:lda:vocab_size: 4258
    INFO:lda:n_words: 84010
    INFO:lda:n_topics: 20
    INFO:lda:n_iter: 1500
    INFO:lda:<0> log likelihood: -1051748
    INFO:lda:<10> log likelihood: -719800
    INFO:lda:<20> log likelihood: -699115
    INFO:lda:<30> log likelihood: -689370
    INFO:lda:<40> log likelihood: -684918
    INFO:lda:<50> log likelihood: -681322
    INFO:lda:<60> log likelihood: -678979
    INFO:lda:<70> log likelihood: -676598
    INFO:lda:<80> log likelihood: -675383
    INFO:lda:<90> log likelihood: -673316
    INFO:lda:<100> log likelihood: -672761
    INFO:lda:<110> log likelihood: -671320
    INFO:lda:<120> log likelihood: -669744
    INFO:lda:<130> log likelihood: -669292
    INFO:lda:<140> log likelihood: -667940
    INFO:lda:<150> log likelihood: -668038
    INFO:lda:<160> log likelihood: -667429
    INFO:lda:<170> log likelihood: -666475
    INFO:lda:<180> log likelihood: -665562
    INFO:lda:<190> log likelihood: -664920
    INFO:lda:<200> log likelihood: -664979
    INFO:lda:<210> log likelihood: -664722
    INFO:lda:<220> log likelihood: -664459
    INFO:lda:<230> log likelihood: -664360
    INFO:lda:<240> log likelihood: -663600
    INFO:lda:<250> log likelihood: -664164
    INFO:lda:<260> log likelihood: -663826
    INFO:lda:<270> log likelihood: -663458
    INFO:lda:<280> log likelihood: -663393
    INFO:lda:<290> log likelihood: -662904
    INFO:lda:<300> log likelihood: -662294
    INFO:lda:<310> log likelihood: -662031
    INFO:lda:<320> log likelihood: -662430
    INFO:lda:<330> log likelihood: -661601
    INFO:lda:<340> log likelihood: -662108
    INFO:lda:<350> log likelihood: -662152
    INFO:lda:<360> log likelihood: -661899
    INFO:lda:<370> log likelihood: -661012
    INFO:lda:<380> log likelihood: -661278
    INFO:lda:<390> log likelihood: -661085
    INFO:lda:<400> log likelihood: -660418
    INFO:lda:<410> log likelihood: -660510
    INFO:lda:<420> log likelihood: -660343
    INFO:lda:<430> log likelihood: -659789
    INFO:lda:<440> log likelihood: -659336
    INFO:lda:<450> log likelihood: -659039
    INFO:lda:<460> log likelihood: -659329
    INFO:lda:<470> log likelihood: -658707
    INFO:lda:<480> log likelihood: -658879
    INFO:lda:<490> log likelihood: -658819
    INFO:lda:<500> log likelihood: -658407
    INFO:lda:<510> log likelihood: -658651
    INFO:lda:<520> log likelihood: -658111
    INFO:lda:<530> log likelihood: -658018
    INFO:lda:<540> log likelihood: -658111
    INFO:lda:<550> log likelihood: -657925
    INFO:lda:<560> log likelihood: -657860
    INFO:lda:<570> log likelihood: -657494
    INFO:lda:<580> log likelihood: -657723
    INFO:lda:<590> log likelihood: -657591
    INFO:lda:<600> log likelihood: -657557
    INFO:lda:<610> log likelihood: -657505
    INFO:lda:<620> log likelihood: -657730
    INFO:lda:<630> log likelihood: -657304
    INFO:lda:<640> log likelihood: -657208
    INFO:lda:<650> log likelihood: -657518
    INFO:lda:<660> log likelihood: -657541
    INFO:lda:<670> log likelihood: -657381
    INFO:lda:<680> log likelihood: -657575
    INFO:lda:<690> log likelihood: -656985
    INFO:lda:<700> log likelihood: -656815
    INFO:lda:<710> log likelihood: -656930
    INFO:lda:<720> log likelihood: -656538
    INFO:lda:<730> log likelihood: -656291
    INFO:lda:<740> log likelihood: -656417
    INFO:lda:<750> log likelihood: -656747
    INFO:lda:<760> log likelihood: -656600
    INFO:lda:<770> log likelihood: -656269
    INFO:lda:<780> log likelihood: -656311
    INFO:lda:<790> log likelihood: -656069
    INFO:lda:<800> log likelihood: -656228
    INFO:lda:<810> log likelihood: -656178
    INFO:lda:<820> log likelihood: -655694
    INFO:lda:<830> log likelihood: -655997
    INFO:lda:<840> log likelihood: -656224
    INFO:lda:<850> log likelihood: -656197
    INFO:lda:<860> log likelihood: -655889
    INFO:lda:<870> log likelihood: -656180
    INFO:lda:<880> log likelihood: -656997
    INFO:lda:<890> log likelihood: -655989
    INFO:lda:<900> log likelihood: -655615
    INFO:lda:<910> log likelihood: -655584
    INFO:lda:<920> log likelihood: -656602
    INFO:lda:<930> log likelihood: -656083
    INFO:lda:<940> log likelihood: -656294
    INFO:lda:<950> log likelihood: -656257
    INFO:lda:<960> log likelihood: -656243
    INFO:lda:<970> log likelihood: -656028
    INFO:lda:<980> log likelihood: -655603
    INFO:lda:<990> log likelihood: -656012
    INFO:lda:<1000> log likelihood: -655849
    INFO:lda:<1010> log likelihood: -655376
    INFO:lda:<1020> log likelihood: -655417
    INFO:lda:<1030> log likelihood: -655856
    INFO:lda:<1040> log likelihood: -655197
    INFO:lda:<1050> log likelihood: -655938
    INFO:lda:<1060> log likelihood: -655529
    INFO:lda:<1070> log likelihood: -655092
    INFO:lda:<1080> log likelihood: -655119
    INFO:lda:<1090> log likelihood: -656215
    INFO:lda:<1100> log likelihood: -655602
    INFO:lda:<1110> log likelihood: -655296
    INFO:lda:<1120> log likelihood: -655547
    INFO:lda:<1130> log likelihood: -655580
    INFO:lda:<1140> log likelihood: -655604
    INFO:lda:<1150> log likelihood: -655168
    INFO:lda:<1160> log likelihood: -655281
    INFO:lda:<1170> log likelihood: -655409
    INFO:lda:<1180> log likelihood: -655517
    INFO:lda:<1190> log likelihood: -654922
    INFO:lda:<1200> log likelihood: -655304
    INFO:lda:<1210> log likelihood: -655852
    INFO:lda:<1220> log likelihood: -655184
    INFO:lda:<1230> log likelihood: -655650
    INFO:lda:<1240> log likelihood: -655606
    INFO:lda:<1250> log likelihood: -656086
    INFO:lda:<1260> log likelihood: -655698
    INFO:lda:<1270> log likelihood: -655351
    INFO:lda:<1280> log likelihood: -655686
    INFO:lda:<1290> log likelihood: -654801
    INFO:lda:<1300> log likelihood: -654973
    INFO:lda:<1310> log likelihood: -655186
    INFO:lda:<1320> log likelihood: -655128
    INFO:lda:<1330> log likelihood: -655365
    INFO:lda:<1340> log likelihood: -655338
    INFO:lda:<1350> log likelihood: -655219
    INFO:lda:<1360> log likelihood: -655115
    INFO:lda:<1370> log likelihood: -654930
    INFO:lda:<1380> log likelihood: -655209
    INFO:lda:<1390> log likelihood: -654940
    INFO:lda:<1400> log likelihood: -655055
    INFO:lda:<1410> log likelihood: -655286
    INFO:lda:<1420> log likelihood: -655316
    INFO:lda:<1430> log likelihood: -655257
    INFO:lda:<1440> log likelihood: -654964
    INFO:lda:<1450> log likelihood: -654884
    INFO:lda:<1460> log likelihood: -655493
    INFO:lda:<1470> log likelihood: -655415
    INFO:lda:<1480> log likelihood: -655192
    INFO:lda:<1490> log likelihood: -655728
    INFO:lda:<1499> log likelihood: -655858
    




    <lda.lda.LDA at 0xc608d6e438>



## 1.3 结果解读

topic_word的每一行是一个topic，因此共有20行，每一列是一个word，因此共有4258列。第m行,n列的元素的含义是这个word属于这个topic的概率是多少，因此每一列的和都是1，每个word属于各个topic的概率之和是1.


```python
topic_word = model.topic_word_  # model.components_ also works
topic_word
```




    array([[3.62505347e-06, 3.62505347e-06, 3.62505347e-06, ...,
            3.62505347e-06, 3.62505347e-06, 3.62505347e-06],
           [1.87498968e-02, 1.17916463e-06, 1.17916463e-06, ...,
            1.17916463e-06, 1.17916463e-06, 1.17916463e-06],
           [1.52206232e-03, 5.05668544e-06, 4.05040504e-03, ...,
            5.05668544e-06, 5.05668544e-06, 5.05668544e-06],
           ...,
           [4.17266923e-02, 3.93610908e-06, 9.05698699e-03, ...,
            3.93610908e-06, 3.93610908e-06, 3.93610908e-06],
           [2.37609835e-06, 2.37609835e-06, 2.37609835e-06, ...,
            2.37609835e-06, 2.37609835e-06, 2.37609835e-06],
           [3.46310752e-06, 3.46310752e-06, 3.46310752e-06, ...,
            3.46310752e-06, 3.46310752e-06, 3.46310752e-06]])




```python
topic_word.shape
```




    (20, 4258)



## 1.4 20个topic中概率前7的word展示
下面这部分代码是计算每个主题中的前7个单词


```python
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
```

    Topic 0: british churchill sale million major letters west
    Topic 1: church government political country state people party
    Topic 2: elvis king fans presley life concert young
    Topic 3: yeltsin russian russia president kremlin moscow michael
    Topic 4: pope vatican paul john surgery hospital pontiff
    Topic 5: family funeral police miami versace cunanan city
    Topic 6: simpson former years court president wife south
    Topic 7: order mother successor election nuns church nirmala
    Topic 8: charles prince diana royal king queen parker
    Topic 9: film french france against bardot paris poster
    Topic 10: germany german war nazi letter christian book
    Topic 11: east peace prize award timor quebec belo
    Topic 12: n't life show told very love television
    Topic 13: years year time last church world people
    Topic 14: mother teresa heart calcutta charity nun hospital
    Topic 15: city salonika capital buddhist cultural vietnam byzantine
    Topic 16: music tour opera singer israel people film
    Topic 17: church catholic bernardin cardinal bishop wright death
    Topic 18: harriman clinton u.s ambassador paris president churchill
    Topic 19: city museum art exhibition century million churches
    

## 1.5 输出前10个文档所属的topic


```python
doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))
for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print("doc: {} topic: {}".format(n, topic_most_pr))
```

    type(doc_topic): <class 'numpy.ndarray'>
    shape: (395, 20)
    doc: 0 topic: 8
    doc: 1 topic: 13
    doc: 2 topic: 14
    doc: 3 topic: 8
    doc: 4 topic: 14
    doc: 5 topic: 14
    doc: 6 topic: 14
    doc: 7 topic: 14
    doc: 8 topic: 14
    doc: 9 topic: 8
    

也可以使用下面的代码实现这个目标，Using the title of the new stories, we can sample the most probable topic。doc_topic这个矩阵是395行，20列，每一行是一个document，每一列是一个topic。Looking at the size of the output we can see that there is a distribution over the 20 topics for each of the 395 documents. These should be normalized for each document, let’s test the first 5，发现前5行，每一行相加都是1.说明第m行，第n列的元素的含义是第m个document属于第n个topic的概率是多少。


```python
doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))
```

    type(doc_topic): <class 'numpy.ndarray'>
    shape: (395, 20)
    


```python
for n in range(5):
    sum_pr = sum(doc_topic[n,:])
    print("document: {} sum: {}".format(n, sum_pr))
```

    document: 0 sum: 1.0
    document: 1 sum: 1.0
    document: 2 sum: 1.0000000000000002
    document: 3 sum: 1.0000000000000002
    document: 4 sum: 0.9999999999999997
    


```python
for n in range(10):
    topic_most_pr = doc_topic[n].argmax()
    print("doc: {} topic: {}\n{}...".format(n,
                                            topic_most_pr,
                                            titles[n][:50]))
```

    doc: 0 topic: 8
    0 UK: Prince Charles spearheads British royal revo...
    doc: 1 topic: 13
    1 GERMANY: Historic Dresden church rising from WW2...
    doc: 2 topic: 14
    2 INDIA: Mother Teresa's condition said still unst...
    doc: 3 topic: 8
    3 UK: Palace warns British weekly over Charles pic...
    doc: 4 topic: 14
    4 INDIA: Mother Teresa, slightly stronger, blesses...
    doc: 5 topic: 14
    5 INDIA: Mother Teresa's condition unchanged, thou...
    doc: 6 topic: 14
    6 INDIA: Mother Teresa shows signs of strength, bl...
    doc: 7 topic: 14
    7 INDIA: Mother Teresa's condition improves, many ...
    doc: 8 topic: 14
    8 INDIA: Mother Teresa improves, nuns pray for "mi...
    doc: 9 topic: 8
    9 UK: Charles under fire over prospect of Queen Ca...
    

## 1.6 输出指定文档所属各个topic的概率


```python
import matplotlib.pyplot as plt
f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([1, 3, 4, 8, 9]):
    ax[i].stem(doc_topic[k,:], linefmt='r-',
               markerfmt='ro', basefmt='w-')
    ax[i].set_xlim(-1, 21)
    ax[i].set_ylim(0, 1)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("Document {}".format(k))
 
ax[4].set_xlabel("Topic")
 
plt.tight_layout()
plt.show()
```


![png](output_25_0.png)


这个包似乎不能进行预测、推断，只能对所有的数据都进行训练，然后对训练集进行主题划分。

# 2.package gensim实现lda model

下面的代码内容主要来自于
https://www.pianshen.com/article/636768367/
和官方文档：
https://radimrehurek.com/gensim/models/ldamodel.html

## 2.1 准备数据并分词
准备原始数据，并将各个句子进行分词，得到一个二维矩阵。


```python
from gensim import corpora, models
import jieba.posseg as jp, jieba
# 文本集
texts = [
    '美国教练坦言，没输给中国女排，是输给了郎平',
    '美国无缘四强，听听主教练的评价',
    '中国女排晋级世锦赛四强，全面解析主教练郎平的执教艺术',
    '为什么越来越多的人买MPV，而放弃SUV？跑一趟长途就知道了',
    '跑了长途才知道，SUV和轿车之间的差距',
    '家用的轿车买什么好']
jieba.add_word('四强', 9, 'n')
flags = ('n', 'nr', 'ns', 'nt', 'eng', 'v', 'd')  # 词性
stopwords = ('没', '就', '知道', '是', '才', '听听', '坦言', '全面', '越来越', '评价', '放弃', '人') 
words_ls = []
for text in texts:
    words = [word.word for word in jp.cut(text) if word.flag in flags and word.word not in stopwords]
    words_ls.append(words)
print(words_ls)
```

    Building prefix dict from the default dictionary ...
    Loading model from cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache
    Loading model cost 0.831 seconds.
    Prefix dict has been built successfully.
    

    [['美国', '输给', '中国女排', '输给', '郎平'], ['美国', '无缘', '四强', '主教练'], ['中国女排', '晋级', '世锦赛', '四强', '主教练', '郎平', '执教', '艺术'], ['买', 'MPV', 'SUV', '跑', '长途'], ['跑', '长途', 'SUV', '轿车', '差距'], ['家用', '轿车', '买']]
    

## 2.2 将数据整理成lda模型所需要的输入的格式


```python
#去重，存到字典里
dictionary = corpora.Dictionary(words_ls)  # 存到字典的过程其实就是得到了一个vocabulary，并给每个word打上了标签。
print(dictionary)
corpus = [dictionary.doc2bow(words) for words in words_ls] # 建立语料库，也就是说建立一个稀疏向量。使用“词ID：词频”的形式形成稀疏向量。
print(corpus)
```

    Dictionary(19 unique tokens: ['中国女排', '美国', '输给', '郎平', '主教练']...)
    [[(0, 1), (1, 1), (2, 2), (3, 1)], [(1, 1), (4, 1), (5, 1), (6, 1)], [(0, 1), (3, 1), (4, 1), (5, 1), (7, 1), (8, 1), (9, 1), (10, 1)], [(11, 1), (12, 1), (13, 1), (14, 1), (15, 1)], [(12, 1), (14, 1), (15, 1), (16, 1), (17, 1)], [(13, 1), (17, 1), (18, 1)]]
    

## 2.3训练lda模型


```python
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=2)
print(lda)
```

    LdaModel(num_terms=19, num_topics=2, decay=0.5, chunksize=2000)
    

## 2.4 对训练集进行主题的判断


```python
topics = lda.print_topics
print(topics)
```

    <bound method BaseTopicModel.print_topics of <gensim.models.ldamodel.LdaModel object at 0x000000178AA7A3C8>>
    


```python
for topic in lda.print_topics(num_words=5):
    print(topic)
```

    (0, '0.087*"四强" + 0.085*"主教练" + 0.070*"郎平" + 0.067*"美国" + 0.063*"中国女排"')
    (1, '0.091*"买" + 0.081*"长途" + 0.076*"跑" + 0.076*"轿车" + 0.071*"输给"')
    


```python
resu = lda.inference(corpus)
resu
```




    (array([[2.9038672 , 3.0961177 ],
            [4.4168324 , 0.58315706],
            [8.405289  , 0.5946879 ],
            [0.5925695 , 5.407418  ],
            [0.6734817 , 5.3265033 ],
            [0.5569761 , 3.443016  ]], dtype=float32), None)



## 2.5 对测试集做推断


```python
# 主题推断
# print(lda.inference(corpus))
text5 = '中国女排将在郎平的率领下向世界女排三大赛的三连冠发起冲击'
bow = dictionary.doc2bow([word.word for word in jp.cut(text5) if word.flag in flags and word.word not in stopwords])
ndarray = lda.inference([bow])[0]
print(text5)
for e, value in enumerate(ndarray[0]):
    print('\t主题%d推断值%.2f' % (e, value))
    
word_id = dictionary.doc2idx(['长途'])[0]
for i in lda.get_term_topics(word_id):
    print('【长途】与【主题%d】的关系值：%.2f%%' % (i[0], i[1]*100))
```

    中国女排将在郎平的率领下向世界女排三大赛的三连冠发起冲击
    	主题0推断值2.23
    	主题1推断值0.77
    【长途】与【主题0】的关系值：2.53%
    【长途】与【主题1】的关系值：6.22%
    

get_document_topic这个方法可以直接输出输入文档所属各个topics的概率


```python
print(bow)
lda.get_document_topics(bow)
```

    [(0, 1), (3, 1)]
    




    [(0, 0.74210423), (1, 0.2578958)]


