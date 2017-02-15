The Rsync Thread extension provides ...

Pre-Requisites

The Rsync Thread extension requires weeWX v3.2.0 or greater.

Installation Instructions

Installation using the wee_extension utility 

Note:   Symbolic names are used below to refer to some file location on the 
weeWX system. These symbolic names allow a common name to be used to refer to 
a directory that may be different from system to system. The following symbolic 
names are used below:

-   $DOWNLOAD_ROOT. The path to the directory containing the downloaded 
    Rsync Thread extension.
    
1.  Download the latest Rsync Thread extension from the Rsync Thread releases 
page (https://github.com/gjr80/weewx-realtime_gauge-data/releases) into
a directory accessible from the weeWX machine.

    wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-rsync_thread/releases/download/v0.1/rsyncthread-0.1.tar.gz

	where $DOWNLOAD_ROOT is the path to the directory where the Rsync Thread 
    extension is to be downloaded.  

2.  Stop weeWX:

    sudo /etc/init.d/weewx stop

	or

    sudo service weewx stop

3.  Install the Rsync Thread extension downloaded at step 1 using the 
*wee_extension* utility:

    wee_extension --install=$DOWNLOAD_ROOT/rsyncthread-0.1.tar.gz

    This will result in output similar to the following:

        Request to install '/var/tmp/rsyncthread-0.1.tar.gz'
        Extracting from tar archive /var/tmp/rsyncthread-0.1.tar.gz
        Saving installer file to /home/weewx/bin/user/installer/RsyncThread
        Saved configuration dictionary. Backup copy at /home/weewx/weewx.conf.20161123124410
        Finished installing extension '/var/tmp/rsyncthread-0.1.tar.gz'

4. Start weeWX:

    sudo /etc/init.d/weewx start

	or

    sudo service weewx start

This will result in ...

Manual installation

1.  Download the latest Rsync Thread extension from the Rsync Thread releases 
page (https://github.com/gjr80/weewx-realtime_gauge-data/releases) into
a directory accessible from the weeWX machine.

    wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-rsync_thread/releases/download/v0.1/rsyncthread-0.1.tar.gz

	where $DOWNLOAD_ROOT is the path to the directory where the Rsync Thread 
    extension is to be downloaded.  

2.  Unpack the extension as follows:

    tar xvfz rsyncthread-0.1.tar.gz

3.  Copy files from within the resulting folder as follows:

    cp rsyncthread/bin/user/rsyncthread.py $BIN_ROOT/user
    
	replacing the symbolic name $BIN_ROOT with the nominal locations for your 
    installation.

4.  Edit weewx.conf:

    vi weewx.conf

5.  In weewx.conf, modify the [Engine] [[Services]] section by adding the 
RsyncThread service to the list of archive services to be run:

    [Engine]
        [[Services]]
        
            archive_services = weewx.engine.StdArchive, user.rsyncthread.Rsync

6. Start weeWX:

    sudo /etc/init.d/weewx start

	or

    sudo service weewx start

This will result in ...
