#!/bin/bash

## initial
if [[ $# -le 1 ]]
then
    echo Usage: "$0 -s < AA|BB|CC> -N <# of nodes> --print --test"
    exit
fi

while [[ $# -ge 1 ]]
do
    key="$1"
    case $key in
	-s)
	    system="$2"
	    shift
	    ;;
	-N | -n)
	    nodes="$2"
	    shift
	    ;;
	-p | --print)
	    printmode="1"
	    ;;
	-t | --test)
	    testmode="1"
	    ;;
	*)
	    echo Usage: "$0 -s < AA|BB|CC> -N <# of nodes> --print --test"
	    exit
	    ;;
    esac
    shift
done

if [[ $system == "AA" ]]
then
    npt=(10 20 30 40)
    nnd=(1  2  3  4)
    omp=8
elif [[ $system == "BB" ]]
then
    npt=(4 8 12)
    nnd=(6 12 18)
    omp=4
elif [[ $system = "CC" ]]
then
    npt=(1 2  3)
    nnd=(9 10 11)
    omp=1
else
    echo Unknown system
    exit 1
fi

## search index
nid=0
for n in ${nnd[@]}; do
    if [[ $nodes == $n ]]
    then
	break
    fi
    ((nid+=1))
done

if [[ $nid -ge ${#nnd[@]} ]]
then
    echo Error: $nodes " is unknown node set in" $system
    exit 1
fi

npt_set=${npt[$nid]}

if [[ $printmode == "1" ]]
then
    echo "OMP = " $omp
    echo "N. node=" $nodes
    echo "N. particles=" $npt_set
fi

today=`date '+%m_%d_%H_%M_%S'`
#mpirun -bootstrap ssh -n $nodes a.out > log.$today
