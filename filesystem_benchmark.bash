if [ "$1" != "" ]; then
    SRC_LOCATION=$1
else
    SRC_LOCATION=/tmp/jeonb/TMP0
fi
if [ "$2" != "" ]; then
    TARGET_LOCATION=$2
else
    TARGET_LOCATION=/tmp/jeonb/TMP1
fi
echo 'SRC folder = ' $SRC_LOCATION
echo 'TARGET folder =' $TARGET_LOCATION

Nref=8
mkdir -p $SRC_LOCATION
mkdir -p $TARGET_LOCATION

for file in $SRC_LOCATION/*; do 
    rm $file 
done
for file in $TARGET_LOCATION/*; do 
    rm $file
done

for N in `seq $Nref -1 2`
do 
    Nmod=N/3+1
    Nfra=N%3
    filesize=$((1024**Nmod*10**Nfra/10))
    nfiles=$((10**(Nref-N)))
    echo 'file size=' $filesize 'nfiles=' $nfiles
    start_time=`date +%s`
    # generating random files
    for x in `seq 1 $nfiles`; do
	head -c $filesize /dev/urandom > $SRC_LOCATION/file_$x
    done
    end_time=`date +%s`
    echo $((end_time - start_time)) "sec for creating"
    sync
    sync
    # Copying files
    start_time=`date +%s`
    for file in $SRC_LOCATION/*; do 
	cp $file $TARGET_LOCATION
    done
    end_time=`date +%s`
    echo $((end_time - start_time)) "sec for copying"
    sync
    sync
    # Deleting files
    start_time=`date +%s`
    for file in $SRC_LOCATION/*; do 
	rm $file 
    done
    for file in $TARGET_LOCATION/*; do 
	rm $file
    done
    end_time=`date +%s`
    echo $((end_time - start_time)) "sec for deleting"
done
