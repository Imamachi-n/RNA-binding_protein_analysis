#!/usr/local/bin/perl
####################################
#Weeder2weblogo#####################
#var1.0_Perl
#update: 2012.4.8
####################################

use strict;
use warnings;

my $file = $ARGV[0];
my $number = $ARGV[1];

#main####################################################
open (IN,"<./$file\.wee") || die;

my $flg_gene=0;
my $flg=0;
my $filehandle = 1;
my $count = 1;
my %gene_ID;

while(my $line = <IN>){
	#Gene_ID
	if($line =~ /^Your sequences/){
		$flg_gene = 1;
		next;
	}elsif($flg_gene == 1){
		$flg_gene = 2;
		next;
	}elsif($flg_gene == 2 && $line eq "\n"){
		$flg_gene = 0;
		next;
	}elsif($flg_gene == 2){
		my @data = split(/\s+/,$line);
		$gene_ID{$data[1]}=$data[3];
		next;
	}
	
	#Sequence_data
	if($line =~ /^Best occurrences/){
		if($filehandle == 0){
			close(OUT);
			$count++;
		}else{
			$filehandle = 0;
		}
		open (OUT,">./$file\#$count\.fasta") || die;
		$flg = 1;
		next;
	}elsif($flg == 1){
		$flg = 2;
		next;
	}elsif($line eq "\n" && $flg == 2){
		$flg = 0;
		next;
	}elsif($flg == 2){
		if($line =~ /^\s+/){
			$line =~ s/^\s+//;
		}
		my @data = split(/\s+/,$line);
		if($data[2] =~ /^\[/){
			$data[2] =~ s/\[//;
			$data[2] =~ s/\]//;
		}
		print OUT "$gene_ID{$data[0]}\n";
		print OUT "$data[2]\n";
		next;
	}
}
close(IN);
close(OUT);
print "...process successfully completed\n";
