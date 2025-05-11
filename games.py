import pygame.draw

from Definitions.definitions_game_map import*
from menu import main_menu_boolean
from tower_class import*
import time

tempura = -5 ## temporaire


def game_map_1(dragging,main_menu_boolean, choosen_map):

    global dragging_card
    global card_archer_rect
    global card_firemage_rect
    global card_icemage_rect
    global card_rockshooter_rect
    global card_adriboom_rect
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
    global hut_built_boolean
    global time_counting
    global currency
    global tutorials_open
    global current_tutorial

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

                elif card_adriboom_rect.collidepoint(event.pos) :
                    dragging = True
                    dragging_card = "adriboom"

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
                    active_towers.remove(tower1)
                    upgrade_panel_tower_1 = False

                if tower_emp2_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_2:
                    tower2.supr()
                    active_towers.remove(tower2)
                    upgrade_panel_tower_2 = False

                if tower_emp3_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_3:
                    tower3.supr()
                    active_towers.remove(tower3)
                    upgrade_panel_tower_3 = False

                if tower_emp4_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_4:
                    tower4.supr()
                    active_towers.remove(tower4)
                    upgrade_panel_tower_4 = False

                if tower_emp5_delete_rect.collidepoint(event.pos) and upgrade_panel_tower_5:
                    tower5.supr()
                    active_towers.remove(tower5)
                    upgrade_panel_tower_5 = False

            if play_pause_continue_button_rect.collidepoint(event.pos) and not game_active and button == "Start":
                game_active = True
                button = "Pause"

            if game_paused and pause_continue_rect.collidepoint(event.pos) :
                game_paused = False

            if game_paused and pause_menu_rect.collidepoint(event.pos) :

                return False, True, 0

            if game_paused and pause_quit_rect.collidepoint(event.pos) :
                pygame.quit()

            if tutorial_button_rect.collidepoint(event.pos) :
                tutorials_open = True
                current_tutorial = 1

            if tutorials_open and tutorials_exit_rect.collidepoint(event.pos) :
                tutorials_open = False
                game_active = False

            if tutorials_open and tutorials_changing_rect.collidepoint(event.pos) :
                if current_tutorial == 1 : current_tutorial = 2
                else : current_tutorial = 1

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
            elif dragging_card == "adriboom" :
                card_adriboom_rect.center = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and dragging:
            if dragging_card == "archer" and card_archer_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency.value >= tower1.value:
                    tower1.archer()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency.value >= tower2.value:
                    tower2.archer()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency.value >= tower3.value:
                    tower3.archer()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency.value >= tower4.value:
                    tower4.archer()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency.value >= tower5.value:
                    tower5.archer()
                card_archer_rect = card_archer.get_rect(topleft=initial_archer_card_pos)

            elif dragging_card == "firemage" and card_firemage_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency.value >= tower1.value:
                    tower1.fire()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency.value >= tower2.value:
                    tower2.fire()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency.value >= tower3.value:
                    tower3.fire()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency.value >= tower4.value:
                    tower4.fire()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency.value >= tower5.value:
                    tower5.fire()
                card_firemage_rect = card_firemage.get_rect(topleft=initial_firemage_card_pos)

            elif dragging_card == "icemage" and card_icemage_rect.collidepoint(event.pos) :
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency.value >= tower1.value:
                    tower1.slow()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency.value >= tower2.value:
                    tower2.slow()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency.value >= tower3.value:
                    tower3.slow()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency.value >= tower4.value:
                    tower4.slow()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency.value >= tower5.value:
                    tower5.slow()
                card_icemage_rect = card_icemage.get_rect(topleft=initial_icemage_card_pos)

            elif dragging_card == "rockshooter" and card_rockshooter_rect.collidepoint(event.pos) :
                if tower1.tower.collidepoint(event.pos) and not tower1.built and currency.value >= tower1.value:
                    tower1.bomber()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built and currency.value >= tower2.value:
                    tower2.bomber()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built and currency.value >= tower3.value:
                    tower3.bomber()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built and currency.value >= tower4.value:
                    tower4.bomber()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built and currency.value >= tower5.value:
                    tower5.bomber()
                card_rockshooter_rect = card_rockshooter.get_rect(topleft=initial_rockshooter_card_pos)

            elif dragging_card == "adriboom" and card_adriboom_rect.collidepoint(event.pos) :
                if not hut_built_boolean and hut_available_rect.collidepoint(event.pos) and currency.value >= hut.value:
                    active_towers.append(hut)
                    hut.adrien()
                    hut_built_boolean = True
                card_adriboom_rect = card_adriboom.get_rect(topleft=initial_adriboom_card_pos)

            dragging = False
            dragging_card = None

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

            game_paused = not game_paused

    if not game_active:
        if 1380 <= mouse_x <= 1440 and 15 <= mouse_y <= 70:
            screen.blit(play_button_selected, (0, 0))
        else:
            screen.blit(play_button, (0, 0))

    if not game_paused:

        for el in active_towers:
            """
            if el.ammo == el.list_ammo[4]:
                el.spawn_bomber()
                """
            #else:  pas oublier de rajouter l'indentation lorsqu'on enleve le commentaire
            el.trigger()


    if game_active:
        time_counting += 0.5

        for element in list_enemy:
            if not game_paused:
                element.move()

            element.draw()

        if not game_paused:
            tempura += 0.5
            en.wave(tempura)
            if hut_built_boolean:
                hut.spawn_bomber(tempura)

        for el in projectiles:
            if not game_paused:
                el.update(dt)
            el.draw(screen)
            if not el.active:
                projectiles.remove(el)

        for el in bombers:
            if not game_paused:
                el.update(dt)

            if not el.active:
                bombers.remove(el)

    for el in active_towers:

        tower_info = [
            (tower1, upgrade_panel_tower_1, (160, 340)),
            (tower2, upgrade_panel_tower_2, (545, 205)),
            (tower3, upgrade_panel_tower_3, (895, 250)),
            (tower4, upgrade_panel_tower_4, (1260, 430)),
            (tower5, upgrade_panel_tower_5, (1385, 195)),
        ]

        for tower, show_panel, panel_pos in tower_info:
            if show_panel:
                can_afford = currency.value >= el.value
                draw_upgrade_panel(screen, tower, panel_pos, can_afford, upgrade_panel, upgrade_panel_gray)

    for tower in [tower1, tower2, tower3, tower4, tower5]:
        if tower.built:
            tower.draw()
            if tower not in active_towers:
                active_towers.append(tower)

    if not hut_built_boolean :                      #afficher la hut en construction si elle est en construction
        screen.blit(hut_available, hut_available_rect)

    if tutorials_open :
        game_paused = True
        if current_tutorial == 1 :
            screen.blit(tutorial_1, (0, 0))
        if current_tutorial == 2 :
            screen.blit(tutorial_2, (0, 0))
    else :
        screen.blit(tree, (0, 0))
        screen.blit(card_archer, card_archer_rect)
        screen.blit(card_firemage, card_firemage_rect)
        screen.blit(card_icemage, card_icemage_rect)
        screen.blit(card_rockshooter, card_rockshooter_rect)
        screen.blit(card_adriboom,card_adriboom_rect)
        screen.blit(tutorial_button,(0,0))

        if 1320 <= mouse_x <= 1370 and 15 <= mouse_y <= 75:
            screen.blit(tutorial_button_selected,(0,0))

    if hut_built_boolean:
        screen.blit(hut_built, hut_built_rect)

    if game_paused and not tutorials_open:

        screen.blit(pause_screen,(0,0))
        if 600 <= mouse_x <= 920 and 320 <= mouse_y <= 395:
            screen.blit(pause_continue,(0,0))

        if 600 <= mouse_x <= 920 and 400 <= mouse_y <= 475:
            screen.blit(pause_menu,(0,0))

        if 600 <= mouse_x <= 920 and 490 <= mouse_y <= 565:
            screen.blit(pause_quit,(0,0))

    return dragging, main_menu_boolean, choosen_map

def draw_upgrade_panel(screen, tower, panel_pos, can_afford, upgrade_panel, upgrade_panel_gray):
    # Draw tower range circle
    circle_surf = pygame.Surface((tower.range * 2, tower.range * 2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surf, (220, 215, 100, 128), (tower.range, tower.range), tower.range, 5)
    screen.blit(circle_surf, (tower.dest[0] - tower.range + 35, tower.dest[1] - tower.range + 50))

    # Draw appropriate panel
    if tower.level > 2 or not can_afford :
        panel = upgrade_panel_gray
    if can_afford:
        panel = upgrade_panel
    screen.blit(panel, panel_pos)

