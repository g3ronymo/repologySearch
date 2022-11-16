Simple (commandline) programm to search for packages on https://repology.org/.

Get a short help message with::

    repologySearch.py -h

Get all packages that match *gimp* exactly,
and are available in the slackware or fedora repository::

    repologySearch.py -s -r '(slackware64_current)|(fedora_36)' gimp

Get all vim packages from the arch repositorys (where *arch* matches
the whole repository name)::

    repologySearch.py -r '^arch$' vim
    

