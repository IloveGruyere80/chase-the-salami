4edef on_on_overlap(sprite, otherSprite):
    info.change_score_by(9999999)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

scene.set_background_color(13)
mySprite = sprites.create(img("""
        . . . . . . . . f f f . . . . . 
            . . f f f f f f f d f f . . . . 
            . . f d d d d d d d d f . . . . 
            . . f d f d d d d f d f . . . . 
            . . f d d d d d d d d f f . . . 
            . . f d d f d d f d d d f . . . 
            . . f d d d f f d d d d f . . . 
            . . f d d d d d d f f f f f . . 
            . . f f f f f f f f 5 5 f f . . 
            . . f f 5 5 5 5 5 5 5 5 f f . . 
            . . . f 8 8 8 8 8 8 8 8 f . . . 
            . . . f f 8 8 8 8 8 8 8 f . . . 
            . . . . f 8 8 8 8 8 8 f f . . . 
            . . . . . f f 8 8 8 f f f . . . 
            . . . . . . f f f f f . f . . . 
            . . . . . . . . . . . . f . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
salami = sprites.create(img("""
        . . 2 2 b b b b b . . . . . . . 
            . 2 b 4 4 4 4 4 4 b . . . . . . 
            2 2 4 4 4 4 d d 4 4 b . . . . . 
            2 b 4 4 4 4 4 4 d 4 b . . . . . 
            2 b 4 4 4 4 4 4 4 d 4 b . . . . 
            2 b 4 4 4 4 4 4 4 4 4 b . . . . 
            2 b 4 4 4 4 4 4 4 4 4 e . . . . 
            2 2 b 4 4 4 4 4 4 4 b e . . . . 
            . 2 b b b 4 4 4 b b b e . . . . 
            . . e b b b b b b b e e . . . . 
            . . . e e b 4 4 b e e e b . . . 
            . . . . . e e e e e e b d b b . 
            . . . . . . . . . . . b 1 1 1 b 
            . . . . . . . . . . . c 1 d d b 
            . . . . . . . . . . . c 1 b c . 
            . . . . . . . . . . . . c c . .
    """),
    SpriteKind.food)