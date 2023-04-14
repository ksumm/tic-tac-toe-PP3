"""import colorama"""
import colorama
from colorama import Fore
colorama.init()

# ASCII Game Logo Art

LOGO = print(Fore.MAGENTA + """
 ********** **   ******        **********     **       ******        **********   *******   ********
/////**/// /**  **////**      /////**///     ****     **////**      /////**///   **/////** /**/////
    /**    /** **    //           /**       **//**   **    //           /**     **     //**/**
    /**    /**/**                 /**      **  //** /**                 /**    /**      /**/*******
    /**    /**/**                 /**     **********/**                 /**    /**      /**/**////
    /**    /**//**    **          /**    /**//////**//**    **          /**    //**     ** /**
    /**    /** //******           /**    /**     /** //******           /**     //*******  /********
    //     //   //////            //     //      //   //////            //       ///////   ////////

""" + Fore.RESET)

RULES = print(Fore.MAGENTA + """
######  #     # #       #######  #####
#     # #     # #       #       #     #
#     # #     # #       #       #
######  #     # #       #####    #####
#   #   #     # #       #             #
#    #  #     # #       #       #     #
#     #  #####  ####### #######  #####

1. The game board has nine cells displayed
   in three rows and three columns.
   -------------
   | 1 | 2 | 3 |
   -------------
   | 4 | 5 | 6 |
   -------------
   | 7 | 8 | 9 |
   -------------
2. Two players make turns by entering the cell number
   and placing "X" or "O" in an empty cell on the grid.
3. The goal is to place "X" or "O" three times in an
   horizontal/vertical/diagonal row.
4. The winner is the first player who made a row.

Let's start to play!
""" + Fore.RESET)
