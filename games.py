from Definitions.definitions_game_map import*
from tower_class import*

dragging_card = None

tempura = 0 ## temporaire

def game_map_1(dragging):

    global dragging_card
    global card_archer_rect
    global card_firemage_rect
    global card_icemage_rect
    global card_rockshooter_rect
    global tempura
    global active_towers
    global projectiles

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
                if tower1.tower.collidepoint(event.pos) and not tower1.built:
                    tower1.archer()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built:
                    tower2.archer()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built:
                    tower3.archer()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built:
                    tower4.archer()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built:
                    tower5.archer()
                card_archer_rect = card_archer.get_rect(topleft=initial_archer_card_pos)

            elif dragging_card == "firemage" and card_firemage_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built:
                    tower1.fire()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built:
                    tower2.fire()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built:
                    tower3.fire()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built:
                    tower4.fire()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built:
                    tower5.fire()
                card_firemage_rect = card_firemage.get_rect(topleft=initial_firemage_card_pos)

            elif dragging_card == "icemage" and card_icemage_rect.collidepoint(event.pos):
                if tower1.tower.collidepoint(event.pos) and not tower1.built:
                    tower1.slow()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built:
                    tower2.slow()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built:
                    tower3.slow()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built:
                    tower4.slow()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built:
                    tower5.slow()
                card_icemage_rect = card_icemage.get_rect(topleft=initial_icemage_card_pos)

            elif dragging_card == "rockshooter" and card_rockshooter_rect.collidepoint(event.pos) :
                if tower1.tower.collidepoint(event.pos) and not tower1.built:
                    tower1.bomber()
                elif tower2.tower.collidepoint(event.pos) and not tower2.built:
                    tower2.bomber()
                elif tower3.tower.collidepoint(event.pos) and not tower3.built:
                    tower3.bomber()
                elif tower4.tower.collidepoint(event.pos) and not tower4.built:
                    tower4.bomber()
                elif tower5.tower.collidepoint(event.pos) and not tower5.built:
                    tower5.bomber()
                card_rockshooter_rect = card_rockshooter.get_rect(topleft=initial_rockshooter_card_pos)

            dragging = False
            dragging_card = None


    screen.blit(background_map_1, (0, 0))

        # Ennemies
    tempura += 1
    if tempura % 50 == 0:
        en.spawn(1)
        #en.spawn(2)
    for element in list_enemy:
        element.move()
        screen.blit(element.image, element.pos)

    for el in active_towers :
        el.trigger()

    screen.blit(card_archer, card_archer_rect)
    screen.blit(card_firemage, card_firemage_rect)
    screen.blit(card_icemage, card_icemage_rect)
    screen.blit(card_rockshooter, card_rockshooter_rect)

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

    if tower1.built:
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


    return dragging


"""     
    if keys[p.K_a]:
        if tower1.tower.collidepoint(event_pos) and not tower1.built:
            tower1.archer()
        elif tower2.tower.collidepoint(event_pos) and not tower2.built:
            tower2.archer()
        elif tower3.tower.collidepoint(event_pos) and not tower3.built:
            tower3.archer()
        elif tower4.tower.collidepoint(event_pos) and not tower4.built:
            tower4.archer()
        elif tower5.tower.collidepoint(event_pos) and not tower5.built:
            tower5.archer()
    if keys[p.K_z]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.bomber()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.bomber()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.bomber()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.bomber()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.bomber()
    if keys[p.K_e]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.slow()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.slow()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.slow()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.slow()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.slow()

    if keys[p.K_r]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.fire()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.fire()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.fire()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.fire()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.fire()

    if keys[p.K_t]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.adrien()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.adrien()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.adrien()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.adrien()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.adrien()

    if keys[p.K_d]:
        if tower1.tower.collidepoint(mouse_pos) and tower1.built:
            tower1.supr()
        elif tower2.tower.collidepoint(mouse_pos) and tower2.built:
            tower2.supr()
        elif tower3.tower.collidepoint(mouse_pos) and tower3.built:
            tower3.supr()
        elif tower4.tower.collidepoint(mouse_pos) and tower4.built:
            tower4.supr()
        elif tower5.tower.collidepoint(mouse_pos) and tower5.built:
            tower5.supr()
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

"""