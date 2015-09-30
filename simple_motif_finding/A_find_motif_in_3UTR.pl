#!/usr/local/bin/perl
#Title: Get representative isoform
#Auther: Naoto Imamachi
#ver: 1.0.0
#Date: 2015-03-03

=pod
=cut

use warnings;
use strict;

my $usage = "Usage: $0 <motif[AAAA,AAAT,AAAC,AAAG...]> <input file> <output file>\n";
my ($motif,$input,$output) = @ARGV or die $usage;

#MAIN#########################################################
open(IN, "<$input") || die "Could not open $input: $!\n";
open(OUT, ">$output") || die "Could not open $output: $!\n";

my @motifs = split/,/,$motif; #the same length
my $motif_length = length($motifs[0]);
print "@motifs\n";
print OUT '###',"Trx_id|UTR_length|Count|Count/UTR_length\n";

while(my $line = <IN>){
	chomp $line;
	my @data = split/\t/,$line;
	my $trx_id = $data[0];
	my $seq = $data[1];
	my $UTR_length = length($seq);
	my $query_size = $UTR_length - $motif_length + 1;
	my $count=0;
	for(my $i=0; $i<=$query_size; $i++){
		my $n_mer = substr($seq,$i,$motif_length);
		foreach(@motifs){
			unless($n_mer eq "$_"){next;}
			$count++;
		}
	}
	my $div = $count / $UTR_length;
	print OUT "$trx_id\t$UTR_length\t$count\t$div\n";
}

close(IN);
close(OUT);
