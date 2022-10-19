from pytube import YouTube as YT


def linke():
    link = input('Enter the link: ')
    yt = YT(link)

    print(f'Title :{yt.title}')
    print(f'Views :{yt.views}')
    print(f'Length :{yt.length}')
    print(f'Rating :{yt.rating}')

    confo = input('Is this the video you want to download? (y/n): ')
    if confo == 'y':
        choice = input('Do you want to download the video or audio? (v/a): ')
        choices = ['v', 'a']
        if choice in choices:
            if choice.lower() == 'v':
                print('Downloading video...')
                stream = yt.streams.get_highest_resolution()
                stream.download('/Users/USERNAME/Videos/Youtube Videos')  #Path can be anywhere make sure to use / instead of \
                print('Download complete!')
            elif choice.lower() == 'a':
                print('Downloading audio...')
                stream = yt.streams.get_audio_only()
                stream.download('/Users/USERNAME/Music/Spotify/English') #Path can be anywhere make sure to use / instead of \
                print('Download complete!')
        else:
            print('Invalid choice')
            linke()
    else:
        print('Aight enter link again properly')
        linke()
    again = input('Do you want to download another video? (y/n): ')
    if again == 'y':
        linke()


linke()
