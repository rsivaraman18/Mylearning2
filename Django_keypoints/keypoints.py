from members.models import Member
data = Member.objects.get(name='python')
data.name = 'java'
data.msg = 'coding'
data.save()


obj = Member(name='java')
obj.update()

# To Update 4th record in a queryset
# from members.models import Member
# x = Member.objects.all()[4]
# x.name = 'java'
# x.save()

obj = Member.objects.filter(status="inactive")
obj.update(status="active")

data.delete()


from members.models import Member
x = Member.objects.all()[2]
x.delete()