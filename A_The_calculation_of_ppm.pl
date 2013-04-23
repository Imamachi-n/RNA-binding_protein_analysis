#!/usr/local/bin/perl
####################################
#A_The_calculation_of_ppm###########
#var1.0_Perl
#update: 2013.4.23
####################################

use strict;
use warnings;

my $file = @ARGV[0];

#main########################################################################################
my $m = 0;
open (IN,"<./$file.tab") || die;
open (OUT,">./$file.bed") || die;

print OUT "chr\ttsc_start\ttsc_end\tfile_name\tppm\tstrand\n";

while (my $line = <IN>){
	chomp $line;
	my ($id,$pat,$gid,$type,$name,$anti,$pid,$alpid,$chr,$str,$rep,$tag,$total,$tsc_start,$tsc_end) = split/\t/,$line;
	my $strand;	
	if($str==1){
		$strand="+";
	}else{
		$strand="-";
	} 	
	my $ppm =  int((($tag * 1000000) / $total) * 100) / 100;	
	if($ppm >=5){
		print OUT "$chr\t$tsc_start\t$tsc_end\t$file\t$ppm\t$strand\n";	
		$m++;
	}	
}
close (IN);
close (OUT);
print "$m\n";
print "...process successfully completed\n";
