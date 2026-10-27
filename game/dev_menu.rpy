## ==============================================================================
## 管理員／開發者：章節與檢查點快速跳轉面板 (Debug Chapter Select)
## ==============================================================================

screen chapter_select():
    tag menu
    modal True

    ## 半透明深藍科幻背景
    add Solid("#080c12f0")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 650
        background Frame(Solid("#111a24d8"), 10, 10)
        padding (30, 25)

        vbox:
            spacing 15

            ## 頂部標題與說明
            hbox:
                xfill True
                vbox:
                    text "【開發管理員】章節進度快速跳轉" size 26 color "#85c1e9" bold True
                    text "點擊任意節點即可直接跳轉至該情境，免去重新走劇情的繁瑣流程。" size 14 color "#a0b2c6"

                textbutton "✕ 關閉" action Return():
                    xalign 1.0
                    text_color "#e74c3c"
                    text_hover_color "#ff6b6b"
                    text_size 18

            null height 5

            ## 兩欄章節佈局
            hbox:
                spacing 40
                xfill True

                ## 第一欄：第一章【開發總監篇】
                vbox:
                    xsize 500
                    spacing 10

                    frame:
                        xfill True
                        background Solid("#182430")
                        padding (12, 8)
                        text "第一章：開發總監篇（決策鏡像）" size 16 color "#5dade2" bold True

                    ## 節點 1
                    button:
                        xfill True
                        background Solid("#141e28")
                        hover_background Solid("#243342")
                        padding (12, 10)
                        action (Start("start") if main_menu else [Hide("chapter_select"), Jump("start")])
                        vbox:
                            text "▶ 1-1. 序章：休眠甦醒與軌道觀測" size 15 color "#ecf0f1" bold True
                            text "穿梭艦低溫解凍、氣態巨行星與翡翠衛星初見、地球危機回憶。" size 12 color "#7f8c8d"

                    ## 節點 2
                    button:
                        xfill True
                        background Solid("#141e28")
                        hover_background Solid("#243342")
                        padding (12, 10)
                        action (Start("dev_jump_chap1_dec1") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap1_dec1")])
                        vbox:
                            text "▶ 1-2. 地面基地：科學家對峙與 90 天通牒" size 15 color "#ecf0f1" bold True
                            text "抵達基地停機坪、超導礦石、首席科學家爭執、第一道德決策。" size 12 color "#7f8c8d"

                    ## 節點 3
                    button:
                        xfill True
                        background Solid("#141e28")
                        hover_background Solid("#243342")
                        padding (12, 10)
                        action (Start("dev_jump_chap1_dec2") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap1_dec2")])
                        vbox:
                            text "▶ 1-3. 第 90 天：推土機衝突與最後通牒" size 15 color "#ecf0f1" bold True
                            text "推土機推進邊界、上校強硬請戰、殘廢老兵被捕、第二道德決策。" size 12 color "#7f8c8d"


                ## 第二欄：第二章【退伍士兵篇】
                vbox:
                    xsize 500
                    spacing 8

                    frame:
                        xfill True
                        background Solid("#182430")
                        padding (12, 8)
                        text "第二章：退伍士兵篇（完整章節）" size 16 color "#7dcea0" bold True

                    viewport:
                        xsize 500
                        ysize 480
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 8
                            xfill True

                            ## 節點 1
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("chapter2_veteran") if main_menu else [Hide("chapter_select"), Jump("chapter2_veteran")])
                                vbox:
                                    text "▶ 2-1. 地球回憶：紙箱葬禮與二十億合約" size 14 color "#ecf0f1" bold True
                                    text "殘疾老兵現狀、孿生哥哥遇害與火化、財團律師上門簽約。" size 11 color "#7f8c8d"

                            ## 節點 2
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_biolab") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_biolab")])
                                vbox:
                                    text "▶ 2-2. 生化實驗室：水槽中的人造載體" size 14 color "#ecf0f1" bold True
                                    text "初抵外星基地、羊水培養槽中沉睡的藍色載體、女科學家冷眼。" size 11 color "#7f8c8d"

                            ## 節點 3
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_link") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_link")])
                                vbox:
                                    text "▶ 2-3. 神經連結：初次奔跑狂喜" size 14 color "#ecf0f1" bold True
                                    text "躺入全尺寸貝殼連結艙、甦醒於三公尺身軀、衝出機庫日光狂奔。" size 11 color "#7f8c8d"

                            ## 節點 4
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_colonel") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_colonel")])
                                vbox:
                                    text "▶ 2-4. 重訓室密會：上校刺探交易抉擇" size 14 color "#ecf0f1" bold True
                                    text "上校私人召見、雙腿誘惑、成為雙面間諜的第一道德決策。" size 11 color "#7f8c8d"

                            ## 節點 5
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_jungle") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_jungle")])
                                vbox:
                                    text "▶ 2-5. 初入翡翠雨林：猛獸遇險與繼承人搭救" size 14 color "#ecf0f1" bold True
                                    text "重甲巨獸追擊跳崖、暗夜螢光狼群圍困、部族繼承人與純白聖種預兆。" size 11 color "#7f8c8d"

                            ## 節點 6
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_hometree") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_hometree")])
                                vbox:
                                    text "▶ 2-6. 家園巨木：三個月共生洗禮與懸空山試煉" size 14 color "#ecf0f1" bold True
                                    text "巨木審判、學習森林之道、夜間雙面情報煎熬、駕馭高空掠翼獸。" size 11 color "#7f8c8d"

                            ## 節點 7
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_betrayal_crisis") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_betrayal_crisis")])
                                vbox:
                                    text "▶ 2-7. 第 90 天：推土機浩劫與間諜真相敗露" size 14 color "#ecf0f1" bold True
                                    text "推土機碾碎聖林、老兵砸毀鏡頭、向部族坦承間諜身分、強制斷開被捕。" size 11 color "#7f8c8d"

                            ## 節點 8
                            button:
                                xfill True
                                background Solid("#141e28")
                                hover_background Solid("#243342")
                                padding (12, 8)
                                action (Start("dev_jump_chap2_final_decision") if main_menu else [Hide("chapter_select"), Jump("dev_jump_chap2_final_decision")])
                                vbox:
                                    text "▶ 2-8. 最後一小時：叛變或順從的終極抉擇" size 14 color "#ecf0f1" bold True
                                    text "上校最後威逼利誘、重返巨木撤離警告、第二倫理動機與是否叛變抉擇。" size 11 color "#7f8c8d"
