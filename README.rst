Simple (commandline) programm to search for packages on https://repology.org/.

Get a short help message with::

    reptologySearch.py -h

Get all packages that match *gimp* exactly,
and are available in the slackware or fedora repository::

    reptologySearch.py -s -r '(slackware64_current)|(fedora_36)' gimp

Get all vim packages from the arch repositorys (where *arch* matches
the whole repository name)::

    reptologySearch.py -r '^arch$' vim
    

