{"filter":false,"title":"factories.py","tooltip":"/djangopractice/factoryapp/factories.py","undoManager":{"mark":11,"position":11,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":44},"action":"insert","lines":["# factories.py","import factory","","","class GroupFactory(factory.django.DjangoModelFactory):","","    class Meta:","        model = Group","","    group_name = 'Backend'","","","class UserFactory(factory.django.DjangoModelFactory):","","    class Meta:","        model = User","","    first_name = factory.Sequence(lambda n: \"Agen %03d\" % n)","    group = factory.Subfactory(GroupFactory)"],"id":1}],[{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"remove","lines":["y"],"id":2},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"remove","lines":["p"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"remove","lines":["."]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"remove","lines":["s"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"remove","lines":["e"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"remove","lines":["i"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"remove","lines":["r"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"remove","lines":["o"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["t"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"remove","lines":["c"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"remove","lines":["a"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["f"]},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["#"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":0,"column":14},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"],"id":6},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":7},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["."]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"remove","lines":["m"],"id":8}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":9},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["i"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["m"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["p"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["o"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["r"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["m"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["d"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["e"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["l"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["m"],"id":11},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["o"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["d"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["e"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["l"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["s"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["."]}],[{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["m"],"id":12},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["o"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["d"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["e"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["l"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["s"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["."]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":0},"end":{"row":8,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1592817277362,"hash":"fc9eb2cb618707d5fbd1ac3b1d9c399f3f7a6218"}