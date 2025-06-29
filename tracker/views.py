from django.shortcuts import render,redirect
from .models import Currentbalance,TrackingHistory

# Create your views here.
def index(request):
    if request.method=="POST":
        description=request.POST.get("description")
        amount=request.POST.get("amount")

        currentbalance,_=Currentbalance.objects.get_or_create(id=1)
        expensestype="CREDIT"

        if float(amount)<0:
            expensestype="DEBIT"
        trackinghistory=TrackingHistory.objects.create(
            currentbalance=currentbalance,
            amount=amount,
            expensestype=expensestype,
            description=description
        )
        currentbalance.currentbalance +=float(trackinghistory.amount)
        currentbalance.save()
        print(description,amount)
        return redirect('/')
    currentbalance,_=Currentbalance.objects.get_or_create(id=1)
    income=0
    expense=0
    for trackinghistory in TrackingHistory.objects.all():
        if trackinghistory.expensestype == "CREDIT":
            income+=trackinghistory.amount
        else:
            expense+=trackinghistory.amount
    contest={'transactions' :TrackingHistory.objects.all(),'currentbalance':currentbalance,'income':income,'expense':expense}
    return render(request,"index.html",contest)

def delete_transaction(request,id):
    trackinghistory=TrackingHistory.objects.filter(id=id)
    if trackinghistory.exists():
        trackinghistory=trackinghistory[0]
        currentbalance,_=Currentbalance.objects.get_or_create(id=1)
        currentbalance.currentbalance -= trackinghistory.amount
        currentbalance.save();


    trackinghistory.delete()
    return redirect('/')