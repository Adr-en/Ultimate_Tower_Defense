from Definitions.definitions_game_map import*
from tower_class import*

bombers = []
tempura = -5 ## temporaire

def game_map_1(dragging):

    global dragging_card
    global card_archer_rect
    global card_firemage_rect
    global card_icemage_rect
    global card_rockshooter_rect
    global tempura
    global active_towers
    global projectiles
    global upgrade_panel_tower_1
    global upgrade_panel_tower_2
    global upgrade_panel_tower_3
    global upgrade_panel_tower_4
    global upgrade_panel_tower_5
    global game_active
    global pause_button_bool
    global continue_button_bool
    global button
    global game_paused

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(background_map_1, (0, 0))
    en.Display_Hp_player()
    en.Coins()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not dragging:
                if card_archer_rect.collidepoint(event.pos):
                    dragging = True
                    dragging_card = "archer"
                elif card_firemage_rect.collidepoint(event.pos):
                    dragging = True
                    dragging_card = "firemage"
                elif card_icemage_rect.collidepoint(event.pos):
                    dragging = True
                    dragging_card = "icemage"
                elif card_rockshooter_rect.collidepoint(event.pos) :
                    dragging = True
                    dragging_card = "rockshooter"

                if tower_emp1_rect.collidepoint(event.pos) and tower1.built :
                    if not upgrade_panel_tower_1:
                        upgrade_panel_tower_1 = True
                    else :
                        upgrade_panel_tower_1 = False

                if tower_emp2_rect.collidepoint(event.pos) and tower2.built :
                    if not upgrade_panel_tower_2:
                        upgrade_panel_tower_2 = True
                    else :
                        upgrade_panel_tower_2 = False

                if tower_emp3_rect.collidepoint(event.pos) and tower3.built:
                    if not upgrade_panel_tower_3:
                        upgrade_panel_tower_3 = True
                    else :
                        upgrade_panel_tower_3 = False

                if tower_emp4_rect.collidepoint(event.pos) and tower4.built:
                    if not upgrade_panel_tower_4:
                        upgrade_panel_tower_4 = True
                    else :
                        upgrade_panel_tower_4 = False

                if tower_emp5_rect.collidepoint(event.pos) and tower5.built:
                    if not upgrade_panel_tower_5:
                        upgrade_panel_tower_5 = True
                    else :
                        upgrade_panel_tower_5 = False

                if tower_emp1_upgrade_rect.collidepoint(event.pos) and upgrade_panel_tower_1:
                    tower1.upgrade()

                if tower_emp2_upgrade_rect.collidepoint(event.pos) and upgrade_panel_tower_2:
                    tower2.upgrade()

                if tower_emp3_upgrade_rect.collidepoint(event.pos) and upgrade_panel_tower_3:
                    tower3.upgrade()

                if tower_emp4_upgrade_rect.collidepoint(event.pos) and upgrade_panel_tower_4:
                    tower4.upgrade()

                if tower_emp5_upgrade_rect.collidepoint(event.pos) and upgrade_panel_tower_5:
                    tower5.upgrade()

                if tower_emp1_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_1:
                    tower1.supr()
                    upgrade_panel_tower_1 = False

                if tower_emp2_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_2:
                    tower2.supr()
                    upgrade_panel_tower_2 = False

                if tower_emp3_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_3:
                    tower3.supr()
                    upgrade_panel_tower_3 = False

                if tower_emp4_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_4:
                    tower4.supr()
                    upgrade_panel_tower_4 = False

                if tower_emp5_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_5:
                    tower5.supr()
                    upgrade_panel_tower_5 = False

            if play_pause_continue_button_rect.collidepoint(event.pos) and not game_active and button == "Start":
                game_active = True
                button = "Pause"

            if play_pause_continue_button_rect.collidepoint(event.pos) and button == "Pause" :
                game_paused = True
                button = "Continue"
                print(game_paused)

            if play_pause_continue_button_rect.collidepoint(event.pos) and button == "Continue" :
                game_paused = False
                button = "Pause"

        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEMOTION and dragging:
            if dragging_card == "archer":
                card_archer_rect.center = event.pos
            elif dragging_card == "firemage":
                card_firemage_rect.center = event.pos
            elif dragging_card == "icemage":
                card_icemage_rect.center = event.pos
            elif dragging_card == "rockshooter":
                card_rockshooter_rect.center = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and dragging:
            if dragging_card == "archer" and card_archer_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency >= tower1.value:
                    tower1.archer()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency >= tower2.value:
                    tower2.archer()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency >= tower3.value:
                    tower3.archer()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency >= tower4.value:
                    tower4.archer()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency >= tower5.value:
                    tower5.archer()
                card_archer_rect = card_archer.get_rect(topleft=initial_archer_card_pos)

            elif dragging_card == "firemage" and card_firemage_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency >= tower1.value:
                    tower1.fire()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency >= tower2.value:
                    tower2.fire()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency >= tower3.value:
                    tower3.fire()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency >= tower4.value:
                    tower4.fire()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency >= tower5.value:
                    tower5.fire()
                card_firemage_rect = card_firemage.get_rect(topleft=initial_firemage_card_pos)

            elif dragging_card == "icemage" and card_icemage_rect.collidepoint(event.pos) :
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency >= tower1.value:
                    tower1.slow()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency >= tower2.value:
                    tower2.slow()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency >= tower3.value:
                    tower3.slow()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency >= tower4.value:
                    tower4.slow()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency >= tower5.value:
                    tower5.slow()
                card_icemage_rect = card_icemage.get_rect(topleft=initial_icemage_card_pos)

            elif dragging_card == "rockshooter" and card_rockshooter_rect.collidepoint(event.pos) :
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency >= tower1.value:
                    tower1.bomber()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency >= tower2.value:
                    tower2.bomber()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency >= tower3.value:
                    tower3.bomber()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency >= tower4.value:
                    tower4.bomber()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency >= tower5.value:
                    tower5.bomber()
                card_rockshooter_rect = card_rockshooter.get_rect(topleft=initial_rockshooter_card_pos)

            dragging = False
            dragging_card = None

    if not game_paused :
        if not game_active :
            if 1380 <= mouse_x <= 1440 and 15 <= mouse_y <= 70:
               screen.blit(play_button_selected,(0,0))
            else :
                screen.blit(play_button, (0,0))
        else :
            button = "Pause"
            screen.blit(pause_button, (0,0))

        for el in active_towers :
            el.trigger()
            level_text = font_level.render(str(el.level), True, "brown")
            screen.blit(level_text, (el.dest[0] + 25, el.dest[1] + 110))

            if currency >= el.value:
                if upgrade_panel_tower_1:
                    screen.blit(upgrade_panel, (105 + 55, 360 - 20))
                if upgrade_panel_tower_2:
                    screen.blit(upgrade_panel, (490 + 55, 225 - 20))
                if upgrade_panel_tower_3:
                    screen.blit(upgrade_panel, (840 + 55, 270 - 20))
                if upgrade_panel_tower_4:
                    screen.blit(upgrade_panel, (1205 + 55, 450 - 20))
                if upgrade_panel_tower_5:
                    screen.blit(upgrade_panel, (1330 + 55, 215 - 20))

            else:
                if upgrade_panel_tower_1:
                    screen.blit(upgrade_panel_gray, (105 + 55, 360 - 20))
                if upgrade_panel_tower_2:
                    screen.blit(upgrade_panel_gray, (490 + 55, 225 - 20))
                if upgrade_panel_tower_3:
                    screen.blit(upgrade_panel_gray, (840 + 55, 270 - 20))
                if upgrade_panel_tower_4:
                    screen.blit(upgrade_panel_gray, (1205 + 55, 450 - 20))
                if upgrade_panel_tower_5:
                    screen.blit(upgrade_panel_gray, (1330 + 55, 215 - 20))


    if tower1.built :
        tower1.draw()
        if tower1 not in active_towers:
            active_towers.append(tower1)
    if tower2.built:
        tower2.draw()
        if tower2 not in active_towers:
            active_towers.append(tower2)
    if tower3.built:
        tower3.draw()
        if tower3 not in active_towers:
            active_towers.append(tower3)
    if tower4.built:
        tower4.draw()
        if tower4 not in active_towers :
            active_towers.append(tower4)
    if tower5.built:
        tower5.draw()
        if tower5 not in active_towers :
            active_towers.append(tower5)

    if game_active :


        for element in list_enemy:
            element.enemy_management()
        tempura += 0.5
        en.wave(tempura)

        for el in projectiles:
            el.update(dt)
            el.draw(screen)
            if not el.active:
                projectiles.remove(el)
        for el in bombers:
            el.update(dt)
            el.draw(screen)
            if not el.active:
                projectiles.remove(el)

    screen.blit(card_archer, card_archer_rect)
    screen.blit(card_firemage, card_firemage_rect)
    screen.blit(card_icemage, card_icemage_rect)
    screen.blit(card_rockshooter, card_rockshooter_rect)

    return dragging
