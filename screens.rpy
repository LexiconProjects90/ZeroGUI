################################################################################
## Initialization##
################################################################################
##
init offset = -1
##
##################################################################################
## Styles##
################################################################################
##
style cmd_text is text:
    size 18
    font "consolas.TTF"
##
style menu_text is text:
    size 20 
    font "consolas.TTF"
##
screen cmd_screen:
    style_prefix "cmd"
    frame:
        xmaximum config.screen_width
        ymaximum config.screen_height
        vbox:
            pass
        vbox:
            text 'Wicrosoft Mindows Version 0.1\nEducational\n'
            text 'C:\\Users\\[username]'
##
##Main Menu##################################################################################################################
##
##Game Menu##################################################################################################################
##    
