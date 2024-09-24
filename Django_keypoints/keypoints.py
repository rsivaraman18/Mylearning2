from members.models import Member
data = Member.objects.get(name='python')
data.name = 'java'
data.msg = 'coding'
data.save()


obj = Member(name='java')
obj.update()

