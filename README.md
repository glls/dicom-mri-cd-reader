# DICOM-MRI-CD-Reader
FDDMRI - Fast Data Dump of MRI-DICOM CDs 
Used to export patient data to text from CD-ROM,
Tested with more than a dozen Lab equipment located in Greece.

## installation
`pip install dicom`

## usage
Change the filepath variable to your CD-ROM's root folder, 
output is tab delimited for easy copy/paste to spreadsheet.


Sample output
```
Patient: 01122334444:	NNNNNN MMMMMMMM
	Study 1:	20141020:	head^general
		Series 99	SR	20141020	PhoenixZIPReport	8	images
		Series 1	MR	20141020	localizer	3	images
		Series 2	MR	20141020	t2_blade_tra_320	24	images
		Series 3	MR	20141020	t1_se_tra	24	images
		Series 4	MR	20141020	t2_blade_tra_dark-fl_320	24	images
		Series 5	MR	20141020	t1_tir_cor	26	images
		Series 6	MR	20141020	t2_blade_sag_320	20	images
		Series 7	MR	20141020	t2_blade_COR_320_FS	26	images
		Series 8	MR	20141020	ep2d_diff_3scan_trace_p2	72	images
		Series 9	MR	20141020	ep2d_diff_3scan_trace_p2_ADC	24	images
```


For extra information check :
http://pydicom.readthedocs.io
