{"filter":false,"title":"get_item_users_interactor.py","tooltip":"/ib_miniprojects_backend/resource_management/interactors/get_item_users_interactor.py","undoManager":{"mark":59,"position":59,"stack":[[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["u"],"id":156},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["s"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["e"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["r"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["_"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["i"]}],[{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["d"],"id":157},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":[":"]}],[{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":[" "],"id":158},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["i"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["n"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["t"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"insert","lines":[","]}],[{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":[" "],"id":159}],[{"start":{"row":13,"column":57},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":160},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":161},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":162}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "],"id":163}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"insert","lines":["    "],"id":164}],[{"start":{"row":15,"column":8},"end":{"row":26,"column":18},"action":"insert","lines":["is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)","        is_not_admin = not is_admin","        if is_not_admin:","            self.presenter.unauthorized_user()","            return","        is_valid_item = self.item_storage.is_valid_item_id(","            item_id=item_id","        )","        is_not_valid_item = not is_valid_item","        if is_not_valid_item:","            self.presenter.invalid_item_id()","            return"],"id":165}],[{"start":{"row":1,"column":24},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":166},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "],"id":167}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["f"],"id":168},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":["r"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":[" "],"id":169},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["r"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["e"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["s"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["u"]}],[{"start":{"row":2,"column":5},"end":{"row":2,"column":10},"action":"remove","lines":["resou"],"id":170},{"start":{"row":2,"column":5},"end":{"row":2,"column":24},"action":"insert","lines":["resource_management"]}],[{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["."],"id":171},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["i"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["n"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["t"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["e"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["r"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["a"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["c"]}],[{"start":{"row":2,"column":32},"end":{"row":2,"column":33},"action":"insert","lines":["t"],"id":172},{"start":{"row":2,"column":33},"end":{"row":2,"column":34},"action":"insert","lines":["o"]},{"start":{"row":2,"column":34},"end":{"row":2,"column":35},"action":"insert","lines":["r"]},{"start":{"row":2,"column":35},"end":{"row":2,"column":36},"action":"insert","lines":["s"]},{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":["."]},{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["s"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["o"],"id":173}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":40},"action":"remove","lines":["sto"],"id":174},{"start":{"row":2,"column":37},"end":{"row":2,"column":45},"action":"insert","lines":["storages"]}],[{"start":{"row":2,"column":45},"end":{"row":2,"column":46},"action":"insert","lines":["."],"id":175},{"start":{"row":2,"column":46},"end":{"row":2,"column":47},"action":"insert","lines":["i"]},{"start":{"row":2,"column":47},"end":{"row":2,"column":48},"action":"insert","lines":["t"]},{"start":{"row":2,"column":48},"end":{"row":2,"column":49},"action":"insert","lines":["e"]},{"start":{"row":2,"column":49},"end":{"row":2,"column":50},"action":"insert","lines":["m"]}],[{"start":{"row":2,"column":50},"end":{"row":2,"column":51},"action":"insert","lines":["_"],"id":176},{"start":{"row":2,"column":51},"end":{"row":2,"column":52},"action":"insert","lines":["s"]},{"start":{"row":2,"column":52},"end":{"row":2,"column":53},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":46},"end":{"row":2,"column":53},"action":"remove","lines":["item_st"],"id":177},{"start":{"row":2,"column":46},"end":{"row":2,"column":68},"action":"insert","lines":["item_storage_interface"]}],[{"start":{"row":2,"column":68},"end":{"row":2,"column":69},"action":"insert","lines":[" "],"id":178},{"start":{"row":2,"column":69},"end":{"row":2,"column":70},"action":"insert","lines":["i"]},{"start":{"row":2,"column":70},"end":{"row":2,"column":71},"action":"insert","lines":["m"]},{"start":{"row":2,"column":71},"end":{"row":2,"column":72},"action":"insert","lines":["p"]},{"start":{"row":2,"column":72},"end":{"row":2,"column":73},"action":"insert","lines":["o"]},{"start":{"row":2,"column":73},"end":{"row":2,"column":74},"action":"insert","lines":["r"]},{"start":{"row":2,"column":74},"end":{"row":2,"column":75},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":75},"end":{"row":2,"column":76},"action":"insert","lines":[" "],"id":179},{"start":{"row":2,"column":76},"end":{"row":2,"column":77},"action":"insert","lines":["\\"]}],[{"start":{"row":2,"column":77},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":180}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "],"id":181}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["I"],"id":182},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["t"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["e"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":8},"action":"remove","lines":["Item"],"id":183},{"start":{"row":3,"column":4},"end":{"row":3,"column":24},"action":"insert","lines":["ItemStorageInterface"]}],[{"start":{"row":10,"column":58},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":184},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"insert","lines":["    "],"id":185}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":12},"action":"insert","lines":["    "],"id":186}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":16},"action":"insert","lines":["    "],"id":187}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":[" "],"id":188},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["i"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["t"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["e"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":21},"action":"remove","lines":["item"],"id":189},{"start":{"row":11,"column":17},"end":{"row":11,"column":29},"action":"insert","lines":["item_storage"]}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":[":"],"id":190}],[{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":[" "],"id":191},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["I"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["t"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["e"]},{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":31},"end":{"row":11,"column":35},"action":"remove","lines":["Item"],"id":192},{"start":{"row":11,"column":31},"end":{"row":11,"column":51},"action":"insert","lines":["ItemStorageInterface"]}],[{"start":{"row":11,"column":51},"end":{"row":11,"column":52},"action":"insert","lines":[","],"id":193}],[{"start":{"row":13,"column":40},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":194},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["s"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["l"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["f"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["."]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["i"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["t"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["e"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":17},"action":"remove","lines":["item"],"id":195},{"start":{"row":14,"column":13},"end":{"row":14,"column":25},"action":"insert","lines":["item_storage"]}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":[" "],"id":196},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":[" "],"id":197},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["i"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["t"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["e"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["m"]}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":32},"action":"remove","lines":["item"],"id":198},{"start":{"row":14,"column":28},"end":{"row":14,"column":40},"action":"insert","lines":["item_storage"]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":8},"action":"remove","lines":["    "],"id":199},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "]},{"start":{"row":25,"column":27},"end":{"row":26,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":12},"action":"remove","lines":["    "],"id":200},{"start":{"row":25,"column":4},"end":{"row":25,"column":8},"action":"remove","lines":["    "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "]},{"start":{"row":24,"column":59},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":8},"end":{"row":28,"column":18},"action":"remove","lines":["is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)","        is_not_admin = not is_admin","        if is_not_admin:","            self.presenter.unauthorized_user()","            return","        is_valid_item = self.item_storage.is_valid_item_id(item_id=item_id)","        is_not_valid_item = not is_valid_item","        if is_not_valid_item:","            self.presenter.invalid_item_id()","            return"],"id":201},{"start":{"row":19,"column":8},"end":{"row":20,"column":35},"action":"insert","lines":["self.validate_admin(user_id)","        self.validate_item(item_id)"]}],[{"start":{"row":27,"column":25},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":202},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"remove","lines":["    "],"id":203},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":204}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":205}],[{"start":{"row":29,"column":4},"end":{"row":43,"column":18},"action":"insert","lines":["def validate_admin(self, user_id: int):","        is_admin = self.user_storage.is_user_admin_or_not(user_id=user_id)","        is_not_admin = not is_admin","        if is_not_admin:","            self.presenter.unauthorized_user()","            return","","    def validate_item(self, item_id: int):","        is_valid_item = self.item_storage.is_valid_item_id(","            item_id=item_id","        )","        is_not_valid_item = not is_valid_item","        if is_not_valid_item:","            self.presenter.invalid_item_id()","            return"],"id":206}],[{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"remove","lines":[" "],"id":207}],[{"start":{"row":17,"column":42},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":208},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":8},"action":"insert","lines":["    "],"id":209}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":12},"action":"insert","lines":["    "],"id":210}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":16},"action":"insert","lines":["    "],"id":211}],[{"start":{"row":18,"column":16},"end":{"row":18,"column":20},"action":"insert","lines":["    "],"id":212}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":24},"action":"insert","lines":["    "],"id":213}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":24},"action":"remove","lines":["    "],"id":214}],[{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":[" "],"id":215},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":[" "]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":[" "]}]]},"ace":{"folds":[],"scrolltop":211,"scrollleft":0,"selection":{"start":{"row":39,"column":27},"end":{"row":39,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1591419123415,"hash":"90ab091b3fa21e8333628ce975f02cef9005e672"}