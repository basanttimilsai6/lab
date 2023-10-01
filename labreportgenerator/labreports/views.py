from django.shortcuts import render, redirect
from .forms import *
from .models import Hematology, Urine, Patient, Report
from django.shortcuts import render, get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO 

from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template

def home(request):
    # Retrieve the Report object based on the 'id'
    return HttpResponse('Login Gara Bro Paila')


def clinic(request):
    if request.method == 'POST':
        c_form_form = CForm(request.POST)
        if c_form_form.is_valid():
            c_form_form.save()
            return redirect('doc')
    c_form_form = CForm(request.POST)
    return render(request, 'hos.html', {'c_form_form': c_form_form})
        


def generate_pdf(request, id):
    # Retrieve the Report object based on the 'id'
    report = get_object_or_404(Report, id=id)
    
    # Create an HTML template with the retrieved content
    html_template = get_template('template.html')  # Replace 'template.html' with your HTML template file
    context = {'report': report}
    html_content = html_template.render(context)

    # Create a PDF response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{report.patient.name}.pdf"'  # Use a relevant field for the filename
    
    # Generate PDF from HTML
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html_content + '</pre>')
    
    return response

     

def view_reports(request):
    reports = Report.objects.all().order_by('-id')

    return render(request, 'view_reports.html', {'reports': reports})
    

def view_report_detail(request, id):
    report = get_object_or_404(Report, pk=id)

    context = {
        'report': report,
    
    }
    return render(request, 'view_report_detail.html', context)

def create_patient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            # Save patient data to the database
            patient_form.save()
            return redirect('create_patient')  # Redirect to a success page after patient creation
    else:
        patient_form = PatientForm()

    return render(request, 'base.html', {'patient_form': patient_form})



def create_report(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        hematology_form = HematologyForm(request.POST, prefix='hematology')
        urine_form = UrineForm(request.POST, prefix='urine')
        bioche_form = BiochemistryForm(request.POST, prefix='biochemistry')
        lipid_form = LipidProfileForm(request.POST,prefix='lipid')
        liver_form = LiverFunctionTestForm(request.POST, prefix='liver')
        widal_form = WidalTestForm(request.POST,prefix='widal')
        test_form = TestForm(request.POST,prefix='test')
        stool_form = StoolForm(request.POST,prefix='stool')
        serology_form = SerologyForm(request.POST, prefix='serology')

        if patient_form.is_valid() and hematology_form.is_valid() and urine_form.is_valid() and bioche_form.is_valid() and lipid_form.is_valid() and liver_form.is_valid() and widal_form.is_valid() and test_form.is_valid() and stool_form.is_valid() and serology_form.is_valid():
            # Save patient data

            hematology = hematology_form.save(commit=False)
            hematology.save()

            patient = patient_form.save()

            # Save Hematology data associated with the patient
            # Save Urine data associated with the patient
            urine = urine_form.save(commit=False)
            urine.patient = patient
            urine.save()

            bio = bioche_form.save(commit=False)
            bio.patient = patient
            bio.save()

            lipid = lipid_form.save(commit=False)
            lipid.patient = patient
            lipid.save()

            test = test_form.save(commit=False)
            test.patient = patient
            test.save()

            stool = stool_form.save(commit=False)
            stool.patient = patient
            stool.save()

            widal = widal_form.save(commit=False)
            widal.patient = patient
            widal.save()

            sero = serology_form.save(commit=False)
            sero.patient = patient
            sero.save()

            liver = liver_form.save(commit=False)
            liver.patient = patient
            liver.save()



            # Create a Report instance
            report = Report(patient=patient, hematology=hematology, urine=urine, bio=bio, lipid=lipid,liver=liver,test=test, widal=widal, sero=sero, stool=stool )
            report.save()

            return redirect('/')  # Redirect to a success page after data submission

    else:
        patient_form = PatientForm()
        hematology_form = HematologyForm(prefix='hematology')
        urine_form = UrineForm(prefix='urine')
        bioche_form = BiochemistryForm(prefix='biochemistry')
        lipid_form = LipidProfileForm(prefix='lipid')
        liver_form = LiverFunctionTestForm(prefix='liver')
        widal_form = WidalTestForm(prefix='widal')
        test_form = TestForm(prefix='test')
        stool_form = StoolForm(prefix='stool')
        serology_form = SerologyForm(prefix='serology')
    context = {
        'patient_form': patient_form,
        'hematology_form': hematology_form,
        'urine_form': urine_form,
        'bioche_form': bioche_form,
        'lipid_form': lipid_form,
        'liver_form': liver_form,
        'widal_form': widal_form,
        'test_form': test_form,
        'stool_form': stool_form,
        'serology_form': serology_form,
    

    }

    return render(request, 'create_report.html',context)
