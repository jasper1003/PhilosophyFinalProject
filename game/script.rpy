# ==========================================
# 角色定義：四個視角的決策載體
# ==========================================
# 1. 資本家 / 開發總監（冰藍色：冷靜計算、宏觀帳目）
define c = Character("開發總監", color="#85c1e9", image="c")

# 2. 殘腿老兵 / 退伍海陸（橄欖灰綠：邊緣旁觀、無名榮民；載體狀態：湛藍色）
define m = Character("退伍士兵", color="#8fa98f", image="m")
define ma = Character("退伍士兵", color="#5dade2", image="ma")

# 3. 原住民首領之女（翡翠綠：生態共感、血統與神聖信條）
define p = Character("原住民公主", color="#7dcea0", image="p")

# 4. 原住民平民（赭黃色：無名個體、生存直覺與平凡視角）
define n = Character("部族獵手", color="#edbb99", image="n")

# 配角與系統
define s = Character("首席科學家", color="#85929e", image="s")
define sa = Character("首席科學家", color="#85929e", image="sa")
define q = Character("上校", color="#c0392b", image="q")
define ai = Character("主控系統", color="#7f8c8d", image="ai")

# 第三章：原住民公主篇配角定義
define warrior = Character("戰士", color="#edbb99", image="n")
define clan_member = Character("另一名族人", color="#a3e4d7")
define chief = Character("酋長", color="#f5b041")
define human_rep = Character("人類代表", color="#85c1e9", image="c")

# ==========================================
# 立繪與頭像設定（像素銳利化、表情與服裝差分）
# ==========================================
# 側邊頭像 (Side Images)
image side c = Transform("images/char_c.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side c stern = Transform("images/char_c_stern.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side c tired = Transform("images/char_c_tired.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side m = Transform("images/char_m.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side m sad = Transform("images/char_m_sad.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side m determined = Transform("images/char_m_determined.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side ma = Transform("images/char_ma.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side ma hospital = Transform("images/char_ma_hospital.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side ma wild = Transform("images/char_ma_wild.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side s = Transform("images/char_s.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side s angry = Transform("images/char_s_angry.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side s urgent = Transform("images/char_s_urgent.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side sa = Transform("images/char_sa.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side sa urgent = Transform("images/char_sa.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side p = Transform("images/char_p.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side n = Transform("images/char_n.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side q = Transform("images/char_q.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side q gym = Transform("images/char_q_gym.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side q angry = Transform("images/char_q_angry.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

image side ai = Transform("images/char_ai.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)
image side ai alert = Transform("images/char_ai_alert.png", zoom=0.18, nearest=True, xpos=10, yalign=1.0)

# 場景立繪 (Full Character Sprites)
image char c = Transform("images/char_c.png", zoom=0.48, nearest=True)
image char c stern = Transform("images/char_c_stern.png", zoom=0.48, nearest=True)
image char c tired = Transform("images/char_c_tired.png", zoom=0.48, nearest=True)

image char m = Transform("images/char_m.png", zoom=0.48, nearest=True)
image char m sad = Transform("images/char_m_sad.png", zoom=0.48, nearest=True)
image char m determined = Transform("images/char_m_determined.png", zoom=0.48, nearest=True)

image char ma = Transform("images/char_ma.png", zoom=0.48, nearest=True)
image char ma hospital = Transform("images/char_ma_hospital.png", zoom=0.48, nearest=True)
image char ma wild = Transform("images/char_ma_wild.png", zoom=0.48, nearest=True)

image char s = Transform("images/char_s.png", zoom=0.48, nearest=True)
image char s angry = Transform("images/char_s_angry.png", zoom=0.48, nearest=True)
image char s urgent = Transform("images/char_s_urgent.png", zoom=0.48, nearest=True)

image char sa = Transform("images/char_sa.png", zoom=0.48, nearest=True)
image char sa urgent = Transform("images/char_sa.png", zoom=0.48, nearest=True)

image char p = Transform("images/char_p.png", zoom=0.48, nearest=True)
image char n = Transform("images/char_n.png", zoom=0.48, nearest=True)

image char q = Transform("images/char_q.png", zoom=0.48, nearest=True)
image char q gym = Transform("images/char_q_gym.png", zoom=0.48, nearest=True)
image char q angry = Transform("images/char_q_angry.png", zoom=0.48, nearest=True)

image char ai = Transform("images/char_ai.png", zoom=0.48, nearest=True)
image char ai alert = Transform("images/char_ai_alert.png", zoom=0.48, nearest=True)

# 氛圍背景設定
image white = Solid("#ffffff")
image bg earth_crisis = "images/bg_earth_crisis.png"
image bg shuttle_cabin = "images/bg_cryo_bay.png"
image bg shuttle_window = "images/bg_orbit_view.png"
image bg hangar_tarmac = "images/bg_hangar_tarmac.png"
image bg ground_base = "images/bg_base_command.png"
image bg base_command = "images/bg_base_command.png"
image bg gym = "images/bg_gym.png"
image bg forest_window = "images/bg_window_jungle.png"
image bg bulldozer_incident = "images/bg_bulldozer_incident.png"

# 後續章節儲備背景
image bg biolab_tanks = "images/bg_biolab_tanks.png"
image bg link_room = "images/bg_link_room.png"
image bg jungle_day = "images/bg_jungle_day.png"
image bg jungle_night = "images/bg_jungle_night.png"
image bg hometree_interior = "images/bg_hometree_interior.png"
image bg floating_mountains = "images/bg_floating_mountains.png"
image bg cremation_contract = "images/bg_cremation_contract.png"
image bg thanator_chase = "images/bg_thanator_chase.png"
image bg woodsprites_night = "images/bg_woodsprites_night.png"
image bg ikran_flight = "images/bg_ikran_flight.png"

# 道德動機記錄變數（用於各角色章節總結與遊戲終局的鏡像對比反詰）
default c_motive = "（尚未進行此抉擇）"
default c_motive_type = ""
default c_choice1_quote = ""
default c_motive2 = "（尚未進行此抉擇）"
default c_motive2_type = ""
default c_choice2_quote = ""

# 第二章：退伍老兵動機記錄變數
default m_motive1 = "（尚未進行此抉擇）"
default m_motive1_type = ""
default m_choice1_quote = ""
default m_motive2 = "（尚未進行此抉擇）"
default m_motive2_type = ""
default m_choice2_quote = ""
default m_rebel_choice = ""
default m_rebel_desc = "（尚未進行此抉擇）"

# 第三章：原住民公主選擇記錄變數
default p_motive1 = "（尚未進行此抉擇）"
default p_motive1_type = ""
default p_choice1_quote = ""
default p_motive2 = "（尚未進行此抉擇）"
default p_motive2_type = ""
default p_choice2_quote = ""

label start:

    scene bg shuttle_cabin
    with fade

    ai "休眠艙解凍完成。航程耗時：五年九個月。歡迎抵達潘朵拉軌道，總監。"

    scene bg shuttle_window
    with dissolve

    c "（軌道掃描顯示，這顆衛星地底深處蜿蜒著高純度的常溫超導礦脈——每公斤價值兩千萬信用點。）"

    scene bg earth_crisis
    with dissolve

    c tired "（而在六光年外的地球，兩百億人正等待這批礦石重啟瀕死的電網。這趟航行耗盡了三大洲整整一年的工業配額——這是一張無法退票的生存支票。）"

    scene bg shuttle_window
    with dissolve

    ai "地面指揮所已就位，等候您的降落指示。"

    c "準備降落。"

    ## ==========================================
    ## 第二節：地面基地——客觀營運匯報與時限通牒
    ## ==========================================
label dev_jump_chap1_dec1:
    scene bg ground_base
    with fade

    show char s at center with dissolve

    s "總監，您剛抵達基地，必須先看這份數據！主礦脈上方的古老巨木，是整片大陸生態神經網絡的中樞，下方更居住著數百名原住民——"

    c "我知道。我也知道受強磁場干擾，礦坑無法側向鑽井，必須垂直開掘。"

    c stern "科學院在這裡駐紮了四年，花掉四億八千萬建學校、教語言，結果他們的搬遷同意率依舊是零。地球電網的失溫名單上，每一秒都有人在死去。"

    s "再給外交途徑一點時間！我們的「異星神經載體」專案已經就緒，接替亡兄簽約的那名退伍海陸士兵基因匹配完美，只要讓他透過載體融入部族——"

    c "我給你們最後三個月。九十天後，如果他們仍不搬遷，重型推土機隊就啟動強制清除。"

    s "……明白了。我們立刻啟動神經連結。"

    hide char s with dissolve

    scene bg forest_window
    with dissolve

    "控制台終端切換為備忘錄簽署頁面：【第一期超導礦區開發排程：給予外交緩衝期九十天，期滿執行地表清除】。"

    menu:
        c "（支撐我做出此項決策的根本考量是——）"

        "「算盤很簡單：和平最划算；但百億人的生計絕不能被少數人拖垮。」":
            $ c_motive_type = "utilitarianism"
            $ c_motive = "依據最大多數人的生存利益量化計算"
            $ c_choice1_quote = "「算盤很簡單：和平最划算；但百億人的生計絕不能被少數人拖垮。」"
            c "（沒錯，一切以大局利益為重。兩百億人的生存遠重於眼前的少數，能省下戰爭成本最好，但底線絕不退讓。）"

        "「一切按規矩來。開採是我的受託職責，給三個月也是法定程序。」":
            $ c_motive_type = "deontology"
            $ c_motive = "恪守受託合約職責與法定程序守則"
            $ c_choice1_quote = "「一切按規矩來。開採是我的受託職責，給三個月也是法定程序。」"
            c "（這無關個人喜好，純粹是履行職責。簽了合約就是律令，該給的程序一天不能少，該交的差一天也不能拖。）"

        "「掌舵者要有談判的度量，也要有動手的魄力；我絕不軟弱逃避。」":
            $ c_motive_type = "virtue_ethics"
            $ c_motive = "展現兼具耐心與決斷之領導者品格"
            $ c_choice1_quote = "「掌舵者要有談判的度量，也要有動手的魄力；我絕不軟弱逃避。」"
            c "（這是我對自己品格的要求。一個合格的領導者必須兼具耐心與剛毅，絕不在關鍵時刻猶豫退縮。）"

        "「凡事應先抱持善意與寬容。只要有一絲生機，就該力求和平。」":
            $ c_motive_type = "christian_agape"
            $ c_motive = "出於對受造生命之仁愛與寬容善行"
            $ c_choice1_quote = "「凡事應先抱持善意與寬容。只要有一絲生機，就該力求和平。」"
            c "（生命是寶貴的。出於仁慈與憐憫，哪怕只有一線生機，我也必須把這扇和平的大門敞開到最後一刻。）"

    "電子印鑑鎖定，全息排程表頂端正式啟動倒數：【90D:00H:00M】。"

    ## ==========================================
    ## 第三節：九十天期滿——推土機衝突與最後通牒
    ## ==========================================
label dev_jump_chap1_dec2:
    scene bg ground_base
    with fade

    "隨後的八十餘天裡，那名退伍士兵順利融入了巨木聚落。然而，在期限逼近的最後一份影音日誌中，他的言辭卻徹底轉向——"

    "『他們不會離開這座巨木。我們手裡沒有任何他們需要的東西。沒有。』"

    scene bg bulldozer_incident
    with dissolve

    "第九十天，【00D:00H:00M】。重型推土機隊如期開拔進場。"

    "突然間，前線傳回刺耳警報——那個由老兵操縱的人造載體，竟然強行攀上推土機砸碎了主導航鏡頭！指揮部當即強制切斷了他的神經連結。"

    scene bg ground_base
    with fade

    show char q at center with dissolve

    q "看看這個，總監——你的外交家家酒徹底玩砸了。外頭那群猴子正在樹冠上集結、給箭頭塗抹神經毒素。"

    q "我的重裝艦隊早就掛滿了高爆燃燒彈。只要你簽字授權，十五分鐘內，我就能把那棵大樹炸成滿地柴火！"

    show char q at right with dissolve
    show char s angry at left with dissolve

    s angry "那棵巨木是整片大陸神經網絡的核心節點！如果將它炸毀，生態鏈斷裂將不可逆轉！這是種族滅絕！"

    "這時，安保衛兵將銬著手銬的退伍老兵推了進來。"

    hide char q with dissolve
    show char m at right with dissolve

    m "巨木底下聚集著數百名毫無武裝的婦孺與孩子。給我最後一個小時！讓我連回載體親口警告他們，把他們帶出巨木的倒塌半徑！"

    hide char m with dissolve
    show char q angry at right with dissolve

    q angry "給他一個小時？那就是給那幫土著六十分鐘去架設防線！我絕不會為了這廢物的聖母同情心，讓我的飛行員去冒被毒箭射穿座艙的風險！"

    c "（地球電網的崩潰已不容許開採再延宕一天，軍事進場已不可逆。但我握有最終決定權：是立即無預警空襲，還是在進攻前給予最後一小時的撤離通牒？）"

    menu:
        c "（我批准最後一小時的撤離通牒，心中最在意的關鍵是——）"

        "「死傷越少麻煩越少。給一小時逃命，才能用最低代價換取開採。」":
            $ c_motive2_type = "utilitarianism"
            $ c_motive2 = "以降低傷亡避免長期報復代價，確保開採長遠效益"
            $ c_choice2_quote = "「死傷越少麻煩越少。給一小時逃命，才能用最低代價換取開採。」"
            c "（這是現實的利害算盤。死傷只會帶來無止境的仇恨與襲擊，多給一小時避難，能為基地省下天文數字的安保代價。）"

        "「我們不是土匪。交戰守則明訂：動武前必須給予平民撤離警告。」":
            $ c_motive2_type = "deontology"
            $ c_motive2 = "遵守非戰鬥人員保護原則之文明交戰義務"
            $ c_choice2_quote = "「我們不是土匪。交戰守則明訂：動武前必須給予平民撤離警告。」"
            c "（規矩就是規矩。無論對手是誰，對無防禦平民進行預先警告是不可逾越的交戰底線，絕不能淪為野蠻行徑。）"

        "「我需要礦石，但我絕不淪為屠夫；身處地獄也要守住做人底線。」":
            $ c_motive2_type = "virtue_ethics"
            $ c_motive2 = "在殘酷現實中維護個人良知與道德尊嚴"
            $ c_choice2_quote = "「我需要礦石，但我絕不淪為屠夫；身處地獄也要守住做人底線。」"
            c "（這是我的為人之道。體制可以逼我做殘酷的決策，但我絕不能放任自己墮落為純粹嗜血的殺戮工具。）"

        "「看在無辜老弱的份上。只要心懷一絲憐憫，就不能趕盡殺絕。」":
            $ c_motive2_type = "christian_agape"
            $ c_motive2 = "出於對無辜弱小者之憐憫與鄰人關愛"
            $ c_choice2_quote = "「看在無辜老弱的份上。只要心懷一絲憐憫，就不能趕盡殺絕。」"
            c "（那是實實在在的活生生性命。出於最純粹的憐憫與同理心，我絕不能眼睜睜看著孩子在無預警的火海中喪命。）"

    ## 決策生效
    c stern "就一個小時。一個小時內禁止越過交戰線；一個小時後，若巨木仍未清空，作戰編隊準時推進。"

    q angry "行啊，總監。指針跳到零的那一秒，我的艦隊就會準時進場洗地！"

    "手銬解開，退伍老兵與科學家即刻衝向生化實驗室。全頻道響起最後倒數：【01:00:00】。"

    hide char s
    hide char q
    with dissolve

label dev_jump_chap1_summary:
    scene black
    with dissolve

    call screen moral_summary_card(
        chapter_title="第一章：企業開發總監篇",
        char_name="企業開發總監",
        char_color="#5dade2",
        char_img="images/char_c.png",
        records=[
            ("第一問題：給予九十天外交緩衝期並確立期滿強制開採", c_motive, c_choice1_quote),
            ("第二問題：推土機衝突後批准空襲前最後一小時撤離通牒", c_motive2, c_choice2_quote)
        ],
        final_action=None
    )

    jump chapter2_veteran

# ==============================================================================
# 第二章：退伍士兵篇——神經連結、孿生幽靈與雙腿的代價
# ==============================================================================
label chapter2_veteran:

    scene black
    with fade

    ## --------------------------------------------------------------------------
    ## 第一節：地球廢墟、紙箱葬禮與二十億的替補合約
    ## --------------------------------------------------------------------------
    scene bg earth_crisis
    with dissolve

    m "（在近海那場爛仗裡，一枚穿甲彈炸碎了我的胸椎。坐上輪椅五年，這個世界就縮小到了膝蓋的高度。）"

    m "（退伍補助金連買輪椅潤滑油都得精打細算。至於能讓我重新站起來的脊椎幹細胞手術？醫生說，那只屬於財團高管。）"

    scene bg cremation_contract
    with dissolve

    m sad "（直到我那受訓三年的分子生態學博士孿生哥哥，在出發前夕為了幾塊零錢死在暗巷搶匪的刀下。）"

    m "（火化爐的熱浪還沒散去，財團代表就帶著特許繼承合約找上了我——因為在潘朵拉上，那具耗資二十億、用哥哥基因培育的異星載體，全世界只有同卵雙胞胎的我能啟動。）"

    m "（他們需要一個能降低資產報廢率的活體大腦；而我，需要逃離這座輪椅監牢。）"

    ## --------------------------------------------------------------------------
    ## 第二節：抵達基地——培育槽中的幽靈與冷眼相對的科學家
    ## --------------------------------------------------------------------------
label dev_jump_chap2_biolab:
    scene bg biolab_tanks
    with fade

    m "（休眠近六年後，我在基地的生化實驗室裡見到了『他』。）"

    m "（哥哥在地球化成了灰燼，但在這座培養槽裡，那張與我一模一樣的臉，卻以三公尺高的完美姿態安詳呼吸著。）"

    show char s angry at right
    with dissolve

    s angry "看夠了嗎，下士？你哥哥花了四年精通植物神經學與原住民語，而財團送給我的替代品，卻是個連培養液酸鹼值都讀不懂的退伍步兵。"

    m "在步兵連裡，長官只教我們一件事：子彈飛過來的時候，別把腦袋露在掩體外面。"

    s "至少你還知道自己有腦袋。躺進連結艙吧，別碰壞了整座基地最昂貴的資產。"

    ## --------------------------------------------------------------------------
    ## 第三節：第一次神經連結——狂喜、腳趾與奔跑的滋味
    ## --------------------------------------------------------------------------
label dev_jump_chap2_link:
    scene bg link_room
    with fade

    s "校準神經突觸脈衝。腦波同步率 99.2\%。關閉艙蓋。"

    "沉重的合金艙蓋合攏，意識瞬間如電流般沿著光纜瘋狂奔湧——"

    scene white
    with dissolve

    "「瞳孔反應正常。神經迴路對接完畢。」"

    scene bg link_room
    with dissolve

    ma hospital "（吸氣——！我的腳趾……在動！）"

    "整整五年再也沒有體會過的神經信號，從足弓一路湧上充盈著爆發力的膝關節！"

    s urgent "下士！先別動！神經突觸還需要五分鐘的重構平衡期！躺下！"

    ma hospital "（躺下？去他的躺下！）"

    "我一把扯掉感應貼片，猛然撐起三公尺高的身軀，撞開防暴護衛直接衝出了實驗室大門！"

    scene bg hangar_tarmac
    with dissolve

    "腳掌重重踏在滾燙的跑道上，我張開雙臂在停機坪上竭盡全力地狂奔、狂笑！"

    ma wild "（我能跑了！我不在乎這具軀體造價多少億，我只知道——我從那具生不如死的輪椅監牢裡逃出來了！）"

    ## --------------------------------------------------------------------------
    ## 第四節：上校的私人密會——重訓室與雙腿的暗黑交易
    ## --------------------------------------------------------------------------
label dev_jump_chap2_colonel:
    scene bg gym
    with fade

    "然而，當連結切斷、意識被拽回癱瘓的肉體時，兩名憲兵已經將我的輪椅推進了安全部隊的重訓室。"

    show char q gym at right
    with dissolve

    q gym "剛才在跑道上動靜鬧得挺大啊，陸戰隊員。"

    q "那些把『生態平衡』掛在嘴邊的科學家已經浪費了四年，連那棵大樹長在哪個地質斷層都沒摸清。我需要一個真正聞過火藥味的人，在林子裡當我的眼睛和耳朵。"

    m "您需要我做什麼，長官？"

    q gym "融入那些藍皮猴子。摸清家園巨木內部的結構盲區、防線與撤退路線，每天晚上把情報送到我的終端機上。"

    q "只要你把這事辦成，等任務結束返航那天，我親自找總監簽字——讓總部最好的醫療團隊用奈米生物材料重塑你的脊椎。"

    q gym "我向你擔保，陸戰隊員：你會用你自己真實的雙腿，站著走回地球。"

    m "（用我自己的腿走出去……這句話像燒紅的鐵條刺穿了我的心臟。）"

    ## --------------------------------------------------------------------------
    ## 第五節：第一個道德決策點——接受刺探任務的底層動機
    ## --------------------------------------------------------------------------
    menu:
        "【面對上校的交易，你決定答應配合。但在你的內心深處，你用什麼理由說服了自己？】"

        "「務實的利益交換：居中建立情報能阻止盲目屠殺，又能合法換回雙腿。」":
            $ m_motive1_type = "utilitarianism"
            $ m_motive1 = "追求各方代價最小化與務實利益平衡"
            $ m_choice1_quote = "「務實的利益交換：居中建立情報能阻止盲目屠殺，又能合法換回雙腿。」"
            m "（在戰場上，活命與結果才是一切。只要我能居中掌握情報，我就能阻止最壞的屠殺發生，同時拿回屬於我的報酬。）"

        "「我依舊是軍人。服從指揮官偵察指令是職責，醫療修復是應得酬勞。」":
            $ m_motive1_type = "deontology"
            $ m_motive1 = "恪守軍人職責契約與安全防衛本分"
            $ m_choice1_quote = "「我依舊是軍人。服從指揮官偵察指令是職責，醫療修復是應得酬勞。」"
            m "（穿上了這身軍裝，我的宣誓就依然有效。上校是基地的合法防衛指揮官，執行偵察任務是職責所在。）"

        "「殘廢苟活談何尊嚴？我必須先重新成為完整站立的人，才配談道德。」":
            $ m_motive1_type = "virtue_ethics"
            $ m_motive1 = "重拾完整人格自尊與擺脫殘缺之境"
            $ m_choice1_quote = "「殘廢苟活談何尊嚴？我必須先重新成為完整站立的人，才配談道德。」"
            m "（當你連自己的生理自尊都無法掌控時，所有的道德都是虛偽的。只有重新擁有一具健全的軀體，我才能主宰作為人的命運。）"

        "「哥哥死得太無辜。為了延續對他的愛，我必須站起來替他走完這條路。」":
            $ m_motive1_type = "christian_agape"
            $ m_motive1 = "出於對孿生亡兄未竟遺願的愛與延續"
            $ m_choice1_quote = "「哥哥死得太無辜。為了延續對他的愛，我必須站起來替他走完這條路。」"
            m "（哥哥在紙箱裡化成了灰燼，但他未完成的夢想還活著。不管背負怎樣的罵名，我都必須代替他走進那片森林。）"

    ## 決策生效
    m determined "收到，長官。我會把您需要的所有情報帶回來。"

    q gym "這才像個海軍陸戰隊。明早六點，直升機會把你們送進叢林。別在那些發光的蟲子裡迷失了你自己。"

    hide char q
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第六節：初入翡翠雨林——猛獸追獵、暗夜圍困與聖種預兆
    ## --------------------------------------------------------------------------
label dev_jump_chap2_jungle:
    scene bg jungle_day
    with fade

    show char ma at left
    show char sa at right
    with dissolve

    sa "看這個信號傳導速率……每一株古樹都透過地底真菌網絡向周圍數萬棵樹傳遞電化學脈衝，整座森林就是一個活生生的巨大大腦！"

    ma "（我單手端著步槍警戒，另一隻手卻在戰術腕錶上悄悄記錄著林冠遮蔽率與地質座標。）"

    sa urgent "不對勁……生物震波讀數破表了！所有人立刻退回樹洞掩體！快！"

    hide char ma
    hide char sa
    with dissolve

    scene bg thanator_chase
    with dissolve

    "十公尺外的蕨類叢轟然炸裂！面對咆哮衝出的六足重甲巨獸，我端起突擊步槍猛烈開火，將牠從手無寸鐵的科研小隊身邊引開！"

    "穿甲彈連牠的骨甲都打不穿，我一路亡命狂奔被逼至百公尺高的瀑布懸崖邊，在巨獸揮爪拍碎步槍的瞬間，縱身躍入萬丈深淵！"

    scene bg jungle_night
    with fade

    show char ma at left
    with dissolve

    ma "（爬上河岸時已是深夜。步槍與無線電全毀，我只能削尖鐵木為矛、點燃樹脂火把，卻在暗夜中引來了十幾頭六足掠食狼群的圍攻！）"

    "兩頭惡狼將我撲倒在地，腥臭的利齒距離咽喉僅剩三公分——"

    "『咻——！咻——！』兩支精準的木箭瞬間貫穿領頭惡狼！一道矯健的身影凌空躍下，喝退了剩餘的狼群。"

    show char p at right
    with dissolve

    p "（半跪在垂死的野獸旁，用匕首結束牠的痛苦並低聲禱告）願你的靈魂回歸萬物母神的懷抱，原諒這場無謂的殺戮……"

    ma "謝了。要不是妳剛才那兩箭，我已經變成牠們的宵夜了。"

    p "（猛然起身，揮起弓身狠狠抽在我臉上）不要道謝！這一切都是你的錯！你像個盲目愚蠢的嬰孩舉著火把亂闖，是你把牠們引來送死的！"

    ma "等等！別丟下我——妳既然恨我們這些『天外行者』，為什麼剛才沒一箭射死我？"

    p "我的箭尖原本對準的就是你的心臟。直到……"

    hide char ma
    hide char p
    with dissolve

    scene bg woodsprites_night
    with dissolve

    "她琥珀色的瞳孔猛然放大——無數枚被部族奉為『母神純白聖種』的森林精靈自夜空飄落，靜靜停駐在我的肩膀與矛尖上。"

    show char ma at left
    show char p at right
    with dissolve

    p "母神的聖潔種子……竟然落在了這個異鄉人身上。跟我來吧，天外行者，看來萬物母神對你另有安排。"

    hide char ma
    hide char p
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第七節：家園巨木與懸空群峰——三個月的共生洗禮
    ## --------------------------------------------------------------------------
label dev_jump_chap2_hometree:
    scene bg hometree_interior
    with fade

    show char n at left
    show char p at right
    with dissolve

    n "（長矛直抵我的咽喉）為什麼把這個『行走的謊言』帶進家園巨木？！這是鋼鐵惡魔用我們的血肉偽造的傀儡，應該現在就挖出他的心臟！"

    p "放下長矛。數十枚母神的純白聖種落在了他身上，長老已降下裁決：給他三個月試煉期，由我教導他我們『看見』世界的方式。"

    p "如果三個月後他依然充滿傲慢，你的長矛隨時可以刺穿他的喉嚨。"

    hide char n
    hide char p
    with dissolve

    scene bg jungle_day
    with fade

    show char ma at left
    show char p at right
    with dissolve

    p "把你的神經髮辮與森林相連，去感受獵物心臟的跳動。記住，我們獵殺是因為生存的必要——世間所有的生命能量都只是向萬物母神借來的，終有一天必須歸還。"

    ma "（『能量只是借來的，終有一天必須歸還……』而在地球，人類把母星吸乾榨淨後，正準備對這顆星球做同樣的事。）"

    hide char ma
    hide char p
    with dissolve

    scene bg link_room
    with fade

    show char m sad at left
    show char q at right
    with dissolve

    q "幹得漂亮，下士。外圍氣根承重柱一共十二根，有了這份結構圖，穿甲燃燒彈就能精準炸斷整棵樹的支撐力學。你的脊椎手術授權書已經在總監桌上了。"

    m sad "（前一個月，我還能告訴自己這只是換回雙腿的交易。可到了第二個月，我已經分不清哪邊才是真實：是輪椅上出賣信任的殘廢間諜，還是在林冠間被接納為族人的靈魂？）"

    hide char m
    hide char q
    with dissolve

    scene bg floating_mountains
    with fade

    show char ma at left
    show char p at right
    with dissolve

    p "第七十五天，這是成年獵手的最終試煉。在雲端築巢的高空掠翼獸一生只認同一位騎手——去吧，與牠締結神經連結，真正成為部族之子！"

    hide char ma
    hide char p
    with dissolve

    scene bg ikran_flight
    with dissolve

    "在萬丈絕壁上，我赤手空拳制服了翼展十二公尺的猛禽巨獸，乘著牠縱身躍入翻湧的雲海！"

    scene bg floating_mountains
    with dissolve

    show char ma at left
    show char n at center
    show char p at right
    with dissolve

    n "我曾以為你只是天外行者的虛假皮囊。但今天你在雲端展翅的姿態證明了你的心——從今往後，你就是我的兄弟！"

    p "我看見了你。不是這具外在的軀殼，而是你那顆無畏、赤誠、與森林同在的心。"

    ma "（『我看見了你。』這五個字像滾燙的利刃劈開了我的胸膛——她不知道，我曾在兩個月前親手把家園巨木的承重柱座標交給了劊子手。）"

    hide char ma
    hide char n
    hide char p
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第八節：第九十天——推土機浩劫、間諜真相敗露與鎖鏈囚徒
    ## --------------------------------------------------------------------------
label dev_jump_chap2_betrayal_crisis:
    scene bg link_room
    with fade

    "第八十九天深夜，我徹底停止傳送座標，對著實驗室鏡頭留下了最後一段日誌："

    m sad "『他們不會離開這座巨木。整座森林就是他們的神經與記憶網絡，我們手裡沒有任何他們需要的東西。沒有。』"

    scene bg bulldozer_incident
    with fade

    "然而第九十天黎明，數台重型裝甲推土機仍沿著我最初提供的外圍座標，蠻橫地碾進了先祖柳樹林！"

    show char ma at left
    show char p at right
    with dissolve

    p "不——！那裡沉睡著我們祖先的聲音！快停下來！"

    "我冒著防禦機槍的彈雨躍上推土機車頂，用石錘瘋狂砸碎了主導航鏡頭——也在最後一秒，讓基地徹底看清了我的背叛。"

    scene bg hometree_interior
    with fade

    show char n at left
    show char p at right
    with dissolve

    n "鋼鐵惡魔毀了聖林！所有戰士給箭頭塗上劇毒，隨我衝出去把那些鐵盒子徹底撕碎！"

    ma "不能去！上校的武裝機隊就等在後面，這是一場你們根本贏不了的屠殺——因為他們早就掌握了家園巨木每一根承重氣根的弱點！"

    p "你……你怎麼會知道他們掌握了巨木的弱點？"

    ma "因為是我告訴他們的！從第一天起，上校派我來的唯一任務，就是摸清巨木結構好讓他們夷平這裡……"

    p "你學會了我們的語言、通過了雲端試煉，難道全都是為了替他們丈量我們的墳墓嗎？！滾出我們的家園！"

    n "（暴怒地將我撲倒捆死，舉起骨刀刺向我的胸膛）我要親手宰了你這披著族人皮囊的惡魔！"

    scene white
    with dissolve

    "千鈞一髮之際，基地強行切斷了神經同步！"

    scene bg ground_base
    with fade

    "憲兵將癱瘓的我拖上輪椅並銬死手銬，推進行政指揮所。"

    show char q angry at right
    show char s angry at left
    with dissolve

    q angry "看看這個吃裡扒外的叛徒！幸好你在第一個月就把巨木十二根主氣根的盲區全交給了我，下士，你的情報工作已經圓滿完成了！"

    s angry "那是數百條性命與整顆星球的生物神經中樞！你們不能用燃燒彈把那裡炸成灰燼！"

    hide char s
    show char m at left
    with dissolve

    m "巨木底下全是不知情的婦孺！總監，給我最後一個小時！讓我連回載體親口警告他們撤出巨木的倒塌半徑！"

    hide char q
    show char c stern at right
    with dissolve

    c stern "就一個小時。一個小時後，無論巨木是否清空，清除程序準時執行。"

    hide char c
    hide char m
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第九節：最後一小時——叛變或順從的終極抉擇
    ## --------------------------------------------------------------------------
label dev_jump_chap2_final_decision:
    scene bg link_room
    with fade

    "全頻道響起【01:00:00】倒數警報。就在我衝回連結艙合上艙蓋的前一秒，上校切入了加密通訊："

    show char q at right
    with dissolve

    q "聽著，陸戰隊員。你的脊椎手術授權書就壓在我終端裡。進去叫那群猴子滾出樹洞，然後你自己立刻跑出轟炸半徑。"

    q angry "只要你不向自己人開火，明天一早你就回地球換一雙真正的腿；但如果你敢拿起武器反抗人類，我會親手把你連同連結艙一起轟成碎渣！"

    hide char q
    with dissolve

    scene white
    with dissolve

    "神經脈衝再次對接。"

    scene bg hometree_interior
    with fade

    show char n at left
    show char p at right
    with dissolve

    ma "（我掙扎著跪坐起身嘶吼）鋼鐵艦隊已經起飛了！不到四十分鐘他們就會炸斷東側主氣根，整棵家園巨木都會倒塌！所有人必須立刻撤往深林！"

    n "閉嘴，間諜！現在又想用謊言動搖軍心，讓我們不戰而逃嗎？！"

    p "（淚水滑過臉頰，握著獵刀走到我面前）在你們的鋼鐵堡壘裡你明明已經安全了，為什麼還要回到這具即將被烈火吞噬的軀體裡來？"

    ma "（只要我只傳達警告、不拔刀反抗，我依然能保住雙腿手術全身而退；但遠處機群的轟鳴已逼近林冠——在這一刻，支撐我做出最終抉擇的靈魂準則是——）"

    ## --------------------------------------------------------------------------
    ## 第二道德決策點：面對毀滅前夕的底層倫理動機
    ## --------------------------------------------------------------------------
    menu:
        "【在個人雙腿的契約、人類軍人的身分，與森林部族的存亡之間，你內心最根本的道德準則是？】"

        "「唯有全力阻止這場單方面屠殺、保護整個生態網絡，才能避免雙方陷入萬劫不復的毀滅。」":
            $ m_motive2_type = "utilitarianism"
            $ m_motive2 = "阻止生態網絡崩潰與最大化雙方存續利益"
            $ m_choice2_quote = "「唯有全力阻止這場單方面屠殺、保護整個生態網絡，才能避免雙方陷入萬劫不復的毀滅。」"
            ma "（一雙腿的利益，絕不能建立在數百條性命與整座森林神經網路的毀滅之上。唯有挺身止戰，才能避免最慘烈的浩劫。）"

        "「我是因欺瞞而欠下血債的人。無論代價為何，為自己的背信贖罪並保護無辜是絕對義務。」":
            $ m_motive2_type = "deontology"
            $ m_motive2 = "承擔欺瞞之罪責並履行保護無辜者的絕對義務"
            $ m_choice2_quote = "「我是因欺瞞而欠下血債的人。無論代價為何，為自己的背信贖罪並保護無辜是絕對義務。」"
            ma "（是我親手洩漏了巨木的結構。君子與戰士的榮譽不容許我帶著骯髒的血債逃回地球，我必須為自己的行為負起全部責任。）"

        "「就算在人類身體裡雙腿殘廢，我絕不能讓靈魂也跪著；唯有勇敢站在弱者身前才配稱為人。」":
            $ m_motive2_type = "virtue_ethics"
            $ m_motive2 = "拒絕靈魂淪喪，以無畏勇氣捍衛良知與人格完整"
            $ m_choice2_quote = "「就算在人類身體裡雙腿殘廢，我絕不能讓靈魂也跪著；唯有勇敢站在弱者身前才配稱為人。」"
            ma "（如果為了換回一雙肉體的腿，卻出賣了接納我的族人，那我這輩子在良知上將徹底殘廢。真正的站立，是靈魂的不屈。）"

        "「他們給了我第二次生命與無私的愛；為了守護所愛之人，我願捨棄自己的一切。」":
            $ m_motive2_type = "christian_agape"
            $ m_motive2 = "出於對部族與伴侶的深切大愛，甘願自我犧牲"
            $ m_choice2_quote = "「他們給了我第二次生命與無私的愛；為了守護所愛之人，我願捨棄自己的一切。」"
            ma "（她教會了我如何去愛這個世界。面對即將降臨的烈火，愛讓我無法獨活，我願意用我的一切去換取他們的生機。）"

    ## --------------------------------------------------------------------------
    ## 決意叛變：拾起戰弓與部族並肩死戰
    ## --------------------------------------------------------------------------
    p "（從我毫無退縮的瞳孔中讀懂了一切，手腕一翻割斷藤蔓，將重木戰弓推到我面前）天外行者已經抵達林冠上方了。告訴我——你究竟是誰的人？"

    ma "那個為了雙腿出賣靈魂的間諜已經死了！先掩護婦孺從地底根系撤離，所有能拉弓的獵手跟上我——我們升空迎敵！"

    n "為了家園巨木！與我們的兄弟並肩作戰！"

    p "我與你同在，直到最後一刻！"

    scene bg ikran_flight
    with dissolve

    "當第一枚燃燒彈撕裂林冠的瞬間，我縱身躍上高空掠翼獸的脊背，向著昔日同袍的鋼鐵艦隊，射出了徹底斬斷人類退路的叛變之箭！"

    scene black
    with fade

label dev_jump_chap2_summary:
    scene black
    with dissolve

    call screen moral_summary_card(
        chapter_title="第二章：退伍士兵篇",
        char_name="退伍士兵",
        char_color="#eb984e",
        char_img="images/char_ma.png",
        records=[
            ("第一問題：面對上校的雙腿修復交易，答應配合潛入部族刺探情報", m_motive1, m_choice1_quote),
            ("第二問題：巨木毀滅前夕，決意背棄雙腿契約與部族並肩死戰", m_motive2, m_choice2_quote)
        ],
        final_action=None
    )

    jump chapter3_princess

# ==============================================================================
# 第三章：原住民公主篇——勇氣與實踐智慧的試煉
# ==============================================================================
label chapter3_princess:

    scene black
    with fade

    ## --------------------------------------------------------------------------
    ## 第一幕：森林的警訊
    ## 場景：森林邊緣，白天。
    ## --------------------------------------------------------------------------
label dev_jump_chap3_act1:
    scene bg jungle_day
    with fade

    "原住民公主與幾名族人巡視森林時，發現人類的開採設備已經越過原本的範圍。附近的動物受到驚擾，部分森林也遭到破壞。"

    scene bg bulldozer_incident
    with dissolve

    show char n at left
    show char p at right
    with dissolve

    "一名戰士憤怒地向她報告。"

    warrior "「他們已經不再遵守承諾了！我們不能繼續等待，應該立刻阻止他們。」"

    clan_member "「可是，如果我們現在發動攻擊，人類可能會帶來更多武器。我們的孩子和長者都會受到威脅。」"

    p "「如果我們不採取行動，難道就要看著他們一步步奪走我們的家園嗎？」"

    "此時，原住民公主必須決定部落接下來的方向。"

    menu:
        "選擇一：面對人類擴大開採，你會怎麼做？"

        "A. 立即號召戰士反抗，不能再容忍人類侵入。":
            $ p_motive1_type = "act_immediately"
            $ p_motive1 = "立即號召戰士反抗，捍衛家園原則"
            $ p_choice1_quote = "「A. 立即號召戰士反抗，不能再容忍人類侵入。」"

        "B. 暫時避免衝突，優先保護族人的安全。":
            $ p_motive1_type = "protect_safety"
            $ p_motive1 = "暫時避免衝突，以族人生命安全為重"
            $ p_choice1_quote = "「B. 暫時避免衝突，優先保護族人的安全。」"

        "C. 派人與人類交涉，同時做好防範準備。":
            $ p_motive1_type = "phronesis_negotiate"
            $ p_motive1 = "審慎交涉並同步建立防禦準備"
            $ p_choice1_quote = "「C. 派人與人類交涉，同時做好防範準備。」"

    hide char n
    hide char p
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第二幕：領導者的孤獨
    ## 場景：部落中央，夜晚。
    ## --------------------------------------------------------------------------
label dev_jump_chap3_act2:
    scene bg hometree_interior
    with fade

    "原住民公主與部落長者討論後，發現部落內部已經出現嚴重分歧。"

    "有些族人認為她應該立即帶領大家反抗，有些人則認為她應該避免戰爭。"

    show char p at right
    with dissolve

    "她的父親提醒她："

    chief "「你不只是一名戰士。你的決定會影響所有族人的生命。」"

    p "「可是，如果我只考慮他們的安全，卻讓人類繼續破壞森林，我又怎麼能稱自己為部落的守護者？」"

    chief "「勇氣不是不害怕，也不是永遠向前。你必須知道什麼時候應該堅持，什麼時候應該等待。」"

    p "「那如果等待本身，就是讓敵人繼續傷害我們呢？」"

    chief "「這就是為什麼領導者不能只依靠憤怒做決定。」"

    hide char p
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第三幕：最後的談判
    ## 場景：森林與人類基地交界處。
    ## --------------------------------------------------------------------------
label dev_jump_chap3_act3:
    scene bg forest_window
    with fade

    "人類派出代表，希望原住民公主接受新的協議。"

    "人類提出：\n1. 暫停部分開採作業。\n2. 保留一定範圍作為原住民的生活領域。\n3. 要求原住民允許人類繼續使用部分森林資源。"

    "但原住民公主知道，這份協議並沒有真正保障部落的長期生存。"

    show char c at left
    show char p at right
    with dissolve

    "談判代表說："

    human_rep "「我們已經做出讓步了。地球上有很多人需要這些資源，你們不可能要求我們完全放棄。」"

    p "「你們稱這是讓步，但你們是否曾經問過我們，為什麼你們有權決定森林可以被拿走多少？」"

    human_rep "「如果完全沒有合作的可能，雙方只會繼續受到傷害。」"

    "原住民公主必須決定是否接受協議。"

    menu:
        "選擇二：你會如何回應人類的協議？"

        "A. 拒絕協議，要求人類停止所有開採。":
            $ p_motive2_type = "reject_all"
            $ p_motive2 = "拒絕妥協，要求人類停止所有開採"
            $ p_choice2_quote = "「A. 拒絕協議，要求人類停止所有開採。」"

        "B. 接受協議，先確保族人目前的安全。":
            $ p_motive2_type = "accept_safety"
            $ p_motive2 = "接受協議，優先確保族人當下安全"
            $ p_choice2_quote = "「B. 接受協議，先確保族人目前的安全。」"

        "C. 要求重新談判，提出明確的領域界線與違約責任。":
            $ p_motive2_type = "renegotiate_terms"
            $ p_motive2 = "要求重新談判，確立領域界線與違約責任"
            $ p_choice2_quote = "「C. 要求重新談判，提出明確的領域界線與違約責任。」"

    hide char c
    hide char p
    with dissolve

    ## --------------------------------------------------------------------------
    ## 第四幕：勇氣的真正意義
    ## 場景：部落高處，可以看見遠方的森林。
    ## --------------------------------------------------------------------------
label dev_jump_chap3_act4:
    scene bg floating_mountains
    with fade

    "原住民公主回到部落，發現族人仍在等待她的決定。"

    "她看著森林，想起自己從小學習的傳統，以及那些曾經教導她如何與潘朵拉共同生活的人。"

    "她也想起部落裡的孩子。"

    show char p at right
    show char ma at left
    with dissolve

    p "「我一直以為，只要有足夠的勇氣，就能保護我們所珍惜的一切。」"

    ma "「那現在呢？」"

    p "「現在我知道，勇氣不只是敢於戰鬥。它也可能是承認自己的判斷不一定正確，願意承擔保護族人的責任。」"

    ma "「那你已經知道該怎麼做了嗎？」"

    p "「我不知道。但我必須做出選擇，而且不能假裝這個選擇沒有代價。」"

    hide char ma
    hide char p
    with dissolve

    "原住民公主轉身走向部落。"

    scene black
    with fade

label dev_jump_chap3_summary:
    scene black
    with dissolve

    call screen moral_summary_card(
        chapter_title="第三章：原住民公主篇",
        char_name="原住民公主",
        char_color="#7dcea0",
        char_img="images/char_p.png",
        records=[
            ("第一問題：面對人類擴大開採，你會怎麼做？", p_motive1, p_choice1_quote),
            ("第二問題：你會如何回應人類的協議？", p_motive2, p_choice2_quote)
        ],
        final_action=None
    )

    "【第三章：原住民公主篇結束】"

    return



