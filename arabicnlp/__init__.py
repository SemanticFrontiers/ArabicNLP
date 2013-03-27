def install_sama(tarfile):
    import subprocess 
    status = subprocess.call(['tar', '-xzf', tarfile, '-C', '/Users/maxlikely/Desktop'])
    if status == 0:
        print 'SAMA installed successfully.'
    else:
        print 'ERROR installing SAMA.'
