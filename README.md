# m3u processor

Don't be misled by the bombastic name. This is just a script that based on a file containing a list of file paths, tells you which ones are not in the same directory as the list and which ones in that directory are not in the list. Both the quantity and the routes. Coincidentally I'm using that with m3u files to see if I have any broken playlists in my digital music library.

In fact, all the code is made with GTP-4. I took care of giving him the precise instructions and he gave me everything in Python, a language in which I am a novice and it would have taken me hours to do it. With ChatGPT it was a matter of 20 minutes.

```shell
python ./m3u_processor/ /Users/ulisesantana/Music/uMusic/Listas/Me\ voy\ pal\ Hierro/Me\ voy\ pal\ Hierro.m3u8
Files in M3U but not in the directory (1):
Bejo/2020 - Rap Largo/01 - Bejo - Rap Largo.flac

Files in the directory but not in the M3U (1):
Bejo/2020 - Rap Largo/01 - Bejo - Rap Largo2.flac
```