try:
    from re import search
    from requests import get, exceptions
    from urllib.request import urlretrieve
    from sys import argv

except KeyboardInterrupt:
    print('\n\033[34mCoded by f4ll_py.\033[m\n')

except Exception as e:
    print(f'\033[31m[-] An error has occurred with a module: \033[m{e}\n')

else:
    if len(argv) == 2:
        if argv[1] == '-h' or argv[1] == '--help':
            print('\n[+] Basic Commands:\n')
            print('[+]   -h                 Help')
            print('[+]   --help             Help')
            print('[+]   -l \033[33m{link}\033[m          Video Link')
            print('[+]   --link \033[33m{link}\033[m      Video Link')
            print('[+]   -hd                HD Quality')
            print('[+]   -sd                SD Quality')
            print('[+]   -n \033[33m{name}\033[m          File Name')
            print('[+]   --name \033[33m{name}\033[m      File Name')
        else:
            print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m')
    else:
        try:
            if len(argv) >= 3:
                if argv[1] == '-l' or argv[1] == '--link':
                    url = argv[2]
                    response = get(url)

                    if len(argv) >= 4:
                        if argv[3] == '-hd':
                            try:
                                link = search ('hd_src:"(.+?)"', response.text)[1]
                            except:
                                print("\n\033[31m[-] This video doesn't have this quality.\033[m")
                        elif argv[3] == '-sd':
                            try:
                                link = search ('sd_src:"(.+?)"', response.text)[1]
                            except:
                                print("\n\033[31m[-] This video doesn't have this quality.\033[m")
                        else:
                            print('\n\033[31m[-] Invalid argument, downloading best quality (File name argument before Quality argument).\033[m')
                            
                            try:
                                link = search ('hd_src:"(.+?)"', response.text)[1]
                            except:
                                link = search ('sd_src:"(.+?)"', response.text)[1]

                        if len(argv) >= 6:   
                            if argv[4] == '-n' or argv[4] == '--name':
                                print('\n\033[32m[+] Downloading video...\033[m\n')
                                urlretrieve(link, f"{argv[5]}.mp4")
                                print('\033[32m[+] Download successfull.\033[m')
                            else:
                                print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                                print('\033[32m[+] Downloading video...\033[m\n')
                                urlretrieve(link, f"Facebook Video.mp4")
                                print('\033[32m[+] Download successfull.\033[m')
                        else:
                            print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                            print('\033[32m[+] Downloading video...\033[m\n')
                            urlretrieve(link, f"Facebook Video.mp4")
                            print('\033[32m[+] Download successfull.\033[m')

                    else:
                        print('\n\033[31m[-] The quality was not stipulated, downloading best quality.\033[m')
                        try:
                            link = search ('hd_src:"(.+?)"', response.text)[1]
                        except:
                            link = search ('sd_src:"(.+?)"', response.text)[1]
                        print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                        print('\033[32m[+] Downloading video...\033[m\n')
                        urlretrieve(link, f"Facebook Video.mp4")
                        print('\033[32m[+] Download successfull.\033[m')
                else:
                    print('\n\033[31m[-] Invalid argument, first argument must be link argument.\033[m')

            else:
                print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parametrs.\033[m')

        except exceptions.MissingSchema:
            print("\n\033[31m[-] This link doesn't redirect to a Facebook video.\033[m")
        except KeyboardInterrupt:
            print('\033[34mCoded by f4ll_py.\033[m\n')
        except Exception as e:
            print(f'An error has occurred: {e}')