import pygame as pg
import random
import sys


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    #落とし穴追加
    hole_sfc= pg.image.load("fig/hole_ana.png")
    hole_sfc= pg.transform.rotozoom(hole_sfc,0,2.0)
    hole_rct= hole_sfc.get_rect()
    hole_rct.center=300,600
    scrn_sfc.blit(hole_sfc,hole_rct)

    #リンゴ追加
    rngo_sfc= pg.image.load("fig/fruit_ringo.png")
    rngo_sfc= pg.transform.rotozoom(rngo_sfc,0,0.6)
    rngo_rct=rngo_sfc.get_rect()
    rngo_rct.center=800,700
    scrn_sfc.blit(rngo_sfc,rngo_rct)


    #毒を追加
    doku_sfc= pg.image.load("fig/doku.png")
    doku_sfc= pg.transform.rotozoom(doku_sfc,0,0.6)
    doku_rct=doku_sfc.get_rect()
    doku_rct.center=1000,700
    doku_sfc.blit(doku_sfc,doku_rct)


    
    

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    ax ,ay = 3, 3

    #速さと大きさと色が違う爆弾を追加
    bomb1_sfc = pg.Surface((50, 50)) # 正方形の空のSurface
    bomb1_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb1_sfc, (128, 128, 128), (30, 30), 20)
    bomb1_rct = bomb1_sfc.get_rect()
    bomb1_rct.centerx = random.randint(0, scrn_rct.width)
    bomb1_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb1_sfc, bomb1_rct) 
    va, vb = +3, +3

    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= ay
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += ay
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= ax
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += ax
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += ay
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= ay
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += ax
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= ax          
        scrn_sfc.blit(tori_sfc, tori_rct) 
        scrn_sfc.blit(hole_sfc,hole_rct)
        if doku_rct:
            scrn_sfc.blit(doku_sfc,doku_rct)
        if rngo_rct:
            scrn_sfc.blit(rngo_sfc,rngo_rct)

        # 練習６
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        bomb1_rct.move_ip(va, vb)
        scrn_sfc.blit(bomb1_sfc, bomb1_rct) 
        yoko, tate = check_bound(bomb1_rct, scrn_rct)
        va *= yoko
        vb *= tate

        if tori_rct.colliderect(bomb_rct):
            return
        if tori_rct.colliderect(bomb1_rct):
            return
        if tori_rct.colliderect(hole_rct):
            return

        #リンゴを取ると早くなる
        if rngo_rct:
            if tori_rct.colliderect(rngo_rct):
                ax+=3
                ay+=3
                rngo_rct = None

        #毒を取ると遅くなる
        if doku_rct:
            if tori_rct.colliderect(doku_rct):
                ax-=2
                ay-=2
                doku_rct = None
            
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()