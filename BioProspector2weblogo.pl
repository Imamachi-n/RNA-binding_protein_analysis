#!/usr/local/bin/perl
####################################
#BioProspector2weblogo##############
#var1.0_Perl
#update: 2012.4.5
####################################

use strict;
use warnings;

my $file = $ARGV[0];
my $number = $ARGV[1];

#main####################################################
open (IN,"<./hg19_UPF1_target_genes_3UTR_10bp_motif.result") || die;

my $flg=0;
my $filehandle = 1;
my $count = 1;

while(my $line = <IN>){
	if($line eq "\n"){
		next;
	}
	chomp $line;
	if($line =~ /^Try/
	|| $line =~ /^The highest/
	|| $line =~ /^Width/
	|| $line =~ /^Blk1/
	|| $line =~ /^[1-6]/){
		next;
	}
	if($line =~ /^Motif/){
		if($filehandle == 0){
			close(OUT);
			$count++;
		}else{
			$filehandle = 0;
		}
		open (OUT,">./hg19_UPF1_target_genes_3UTR_10bp_motif#$count\.fasta") || die;
	}else{
		if($line =~ /^>/){
			print OUT "$line\n";
			$flg=1;
		}elsif($flg == 1){
			print OUT "$line\n";
			$flg=0;
		}
	}
}
close(IN);
close(OUT);
print "...process successfully completed\n";
