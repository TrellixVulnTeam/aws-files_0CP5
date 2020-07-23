{"filter":false,"title":"storage_implementation.py","tooltip":"/fb_post_learning/fb_post_v2/storages/storage_implementation.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":164,"column":52},"end":{"row":164,"column":53},"action":"insert","lines":["O"],"id":771}],[{"start":{"row":164,"column":51},"end":{"row":164,"column":53},"action":"remove","lines":["PO"],"id":772},{"start":{"row":164,"column":51},"end":{"row":164,"column":69},"action":"insert","lines":["POSITIVE_REACTIONS"]}],[{"start":{"row":164,"column":51},"end":{"row":164,"column":52},"action":"insert","lines":["("],"id":773}],[{"start":{"row":164,"column":52},"end":{"row":165,"column":0},"action":"insert","lines":["",""],"id":774},{"start":{"row":165,"column":0},"end":{"row":165,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":165,"column":30},"end":{"row":165,"column":31},"action":"insert","lines":[","],"id":775}],[{"start":{"row":165,"column":31},"end":{"row":166,"column":0},"action":"insert","lines":["",""],"id":776},{"start":{"row":166,"column":0},"end":{"row":166,"column":12},"action":"insert","lines":["            "]},{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"remove","lines":["n"],"id":777}],[{"start":{"row":166,"column":12},"end":{"row":166,"column":13},"action":"insert","lines":["N"],"id":778},{"start":{"row":166,"column":13},"end":{"row":166,"column":14},"action":"insert","lines":["E"]},{"start":{"row":166,"column":14},"end":{"row":166,"column":15},"action":"insert","lines":["G"]}],[{"start":{"row":166,"column":12},"end":{"row":166,"column":15},"action":"remove","lines":["NEG"],"id":779},{"start":{"row":166,"column":12},"end":{"row":166,"column":30},"action":"insert","lines":["NEGATIVE_REACTIONS"]}],[{"start":{"row":166,"column":30},"end":{"row":167,"column":0},"action":"insert","lines":["",""],"id":780},{"start":{"row":167,"column":0},"end":{"row":167,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":167,"column":8},"end":{"row":167,"column":12},"action":"remove","lines":["    "],"id":781}],[{"start":{"row":167,"column":8},"end":{"row":167,"column":9},"action":"insert","lines":[")"],"id":782}],[{"start":{"row":167,"column":9},"end":{"row":168,"column":0},"action":"insert","lines":["",""],"id":783},{"start":{"row":168,"column":0},"end":{"row":168,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":168,"column":4},"end":{"row":168,"column":8},"action":"remove","lines":["    "],"id":784},{"start":{"row":168,"column":0},"end":{"row":168,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":168,"column":0},"end":{"row":169,"column":0},"action":"insert","lines":["",""],"id":785}],[{"start":{"row":169,"column":0},"end":{"row":169,"column":4},"action":"insert","lines":["    "],"id":786}],[{"start":{"row":169,"column":4},"end":{"row":169,"column":8},"action":"insert","lines":["    "],"id":787}],[{"start":{"row":169,"column":8},"end":{"row":180,"column":24},"action":"insert","lines":["positive_count = Count('reactions', filter=Q(","        reactions__reaction__in=POSITIVE_REACTIONS))","","    negative_count = Count('reactions', filter=Q(","        reactions__reaction__in=NEGATIVE_REACTIONS))","","    post_objs_ids = list(Post.objects.annotate(p_count=positive_count)\\","                        .annotate(n_count=negative_count)\\","                        .filter(p_count__gt=F('n_count'))\\","                        .values_list('id', flat=True))","","    return post_objs_ids"],"id":788}],[{"start":{"row":172,"column":4},"end":{"row":172,"column":8},"action":"insert","lines":["    "],"id":789}],[{"start":{"row":173,"column":8},"end":{"row":173,"column":12},"action":"insert","lines":["    "],"id":790}],[{"start":{"row":170,"column":8},"end":{"row":170,"column":12},"action":"insert","lines":["    "],"id":791}],[{"start":{"row":175,"column":4},"end":{"row":175,"column":8},"action":"insert","lines":["    "],"id":792}],[{"start":{"row":180,"column":4},"end":{"row":180,"column":8},"action":"insert","lines":["    "],"id":793}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"remove","lines":["    "],"id":794},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"remove","lines":["    "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "],"id":795},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"insert","lines":["    "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "],"id":796},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"insert","lines":["    "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":176,"column":28},"end":{"row":176,"column":29},"action":"insert","lines":[" "],"id":797}],[{"start":{"row":177,"column":28},"end":{"row":177,"column":29},"action":"insert","lines":[" "],"id":798}],[{"start":{"row":178,"column":28},"end":{"row":178,"column":29},"action":"insert","lines":[" "],"id":799}],[{"start":{"row":180,"column":28},"end":{"row":181,"column":0},"action":"insert","lines":["",""],"id":800},{"start":{"row":181,"column":0},"end":{"row":181,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":181,"column":4},"end":{"row":181,"column":8},"action":"remove","lines":["    "],"id":801},{"start":{"row":181,"column":0},"end":{"row":181,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":181,"column":0},"end":{"row":182,"column":0},"action":"insert","lines":["",""],"id":802}],[{"start":{"row":182,"column":0},"end":{"row":182,"column":4},"action":"insert","lines":["    "],"id":803}],[{"start":{"row":182,"column":4},"end":{"row":182,"column":67},"action":"insert","lines":["def get_posts_reacted_by_user(self, user_id: int) -> List[int]:"],"id":804}],[{"start":{"row":182,"column":67},"end":{"row":183,"column":0},"action":"insert","lines":["",""],"id":805},{"start":{"row":183,"column":0},"end":{"row":183,"column":8},"action":"insert","lines":["        "]},{"start":{"row":183,"column":8},"end":{"row":183,"column":9},"action":"insert","lines":["p"]},{"start":{"row":183,"column":9},"end":{"row":183,"column":10},"action":"insert","lines":["a"]},{"start":{"row":183,"column":10},"end":{"row":183,"column":11},"action":"insert","lines":["s"]},{"start":{"row":183,"column":11},"end":{"row":183,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":183,"column":11},"end":{"row":183,"column":12},"action":"remove","lines":["s"],"id":806},{"start":{"row":183,"column":10},"end":{"row":183,"column":11},"action":"remove","lines":["s"]},{"start":{"row":183,"column":9},"end":{"row":183,"column":10},"action":"remove","lines":["a"]},{"start":{"row":183,"column":8},"end":{"row":183,"column":9},"action":"remove","lines":["p"]}],[{"start":{"row":183,"column":8},"end":{"row":187,"column":32},"action":"insert","lines":["user_reacted_post_ids = list(Post.objects.filter(","                reactions__reacted_by_id=user_id)\\","                .values_list('id', flat=True))","","    return user_reacted_post_ids"],"id":807}],[{"start":{"row":187,"column":4},"end":{"row":187,"column":8},"action":"insert","lines":["    "],"id":808}],[{"start":{"row":187,"column":36},"end":{"row":188,"column":0},"action":"insert","lines":["",""],"id":809},{"start":{"row":188,"column":0},"end":{"row":188,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":188,"column":4},"end":{"row":188,"column":8},"action":"remove","lines":["    "],"id":810},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":188,"column":0},"end":{"row":189,"column":0},"action":"insert","lines":["",""],"id":811}],[{"start":{"row":189,"column":0},"end":{"row":189,"column":4},"action":"insert","lines":["    "],"id":812}],[{"start":{"row":189,"column":4},"end":{"row":189,"column":75},"action":"insert","lines":["def get_reactions_to_post(self, post_id: int) -> List[ReactionsToPost]:"],"id":813}],[{"start":{"row":189,"column":75},"end":{"row":190,"column":0},"action":"insert","lines":["",""],"id":814},{"start":{"row":190,"column":0},"end":{"row":190,"column":8},"action":"insert","lines":["        "]},{"start":{"row":190,"column":8},"end":{"row":190,"column":9},"action":"insert","lines":["p"]},{"start":{"row":190,"column":9},"end":{"row":190,"column":10},"action":"insert","lines":["a"]},{"start":{"row":190,"column":10},"end":{"row":190,"column":11},"action":"insert","lines":["s"]},{"start":{"row":190,"column":11},"end":{"row":190,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":20},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":815},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":816}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["f"],"id":817},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["r"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["o"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":[" "],"id":818},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["f"],"id":819},{"start":{"row":4,"column":5},"end":{"row":4,"column":15},"action":"insert","lines":["fb_post_v2"]}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["."],"id":820}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["d"],"id":821},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":18},"action":"remove","lines":["dt"],"id":822},{"start":{"row":4,"column":16},"end":{"row":4,"column":20},"action":"insert","lines":["dtos"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["."],"id":823},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["d"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":23},"action":"remove","lines":["dt"],"id":824},{"start":{"row":4,"column":21},"end":{"row":4,"column":25},"action":"insert","lines":["dtos"]}],[{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":[" "],"id":825},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["i"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["m"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["p"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["o"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["r"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":[" "],"id":826},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["R"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["e"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":33},"end":{"row":4,"column":36},"action":"remove","lines":["Rea"],"id":827},{"start":{"row":4,"column":33},"end":{"row":4,"column":48},"action":"insert","lines":["ReactionsToPost"]}],[{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"remove","lines":["s"],"id":828},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"remove","lines":["s"]},{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"remove","lines":["a"]},{"start":{"row":118,"column":12},"end":{"row":118,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":118,"column":12},"end":{"row":118,"column":13},"action":"insert","lines":["r"],"id":829},{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"insert","lines":["e"]},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"insert","lines":["t"]},{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"insert","lines":["u"]},{"start":{"row":118,"column":16},"end":{"row":118,"column":17},"action":"insert","lines":["r"]},{"start":{"row":118,"column":17},"end":{"row":118,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":118,"column":18},"end":{"row":118,"column":19},"action":"insert","lines":[" "],"id":830},{"start":{"row":118,"column":19},"end":{"row":118,"column":20},"action":"insert","lines":["R"]}],[{"start":{"row":118,"column":19},"end":{"row":118,"column":20},"action":"remove","lines":["R"],"id":831},{"start":{"row":118,"column":19},"end":{"row":118,"column":39},"action":"insert","lines":["ReactionDoesNotExist"]}],[{"start":{"row":191,"column":11},"end":{"row":191,"column":12},"action":"remove","lines":["s"],"id":832},{"start":{"row":191,"column":10},"end":{"row":191,"column":11},"action":"remove","lines":["s"]},{"start":{"row":191,"column":9},"end":{"row":191,"column":10},"action":"remove","lines":["a"]},{"start":{"row":191,"column":8},"end":{"row":191,"column":9},"action":"remove","lines":["p"]}],[{"start":{"row":191,"column":8},"end":{"row":192,"column":57},"action":"insert","lines":["reaction_objs = Reaction.objects.filter(post_id=post_id)\\","                            .select_related('reacted_by')"],"id":833}],[{"start":{"row":192,"column":57},"end":{"row":193,"column":0},"action":"insert","lines":["",""],"id":834},{"start":{"row":193,"column":0},"end":{"row":193,"column":28},"action":"insert","lines":["                            "]}],[{"start":{"row":193,"column":24},"end":{"row":193,"column":28},"action":"remove","lines":["    "],"id":835},{"start":{"row":193,"column":20},"end":{"row":193,"column":24},"action":"remove","lines":["    "]},{"start":{"row":193,"column":16},"end":{"row":193,"column":20},"action":"remove","lines":["    "]},{"start":{"row":193,"column":12},"end":{"row":193,"column":16},"action":"remove","lines":["    "]},{"start":{"row":193,"column":8},"end":{"row":193,"column":12},"action":"remove","lines":["    "]}],[{"start":{"row":83,"column":23},"end":{"row":83,"column":24},"action":"insert","lines":["."],"id":836}],[{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"remove","lines":["s"],"id":837},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"remove","lines":["s"]},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"remove","lines":["a"]},{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"insert","lines":["p"],"id":838},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"insert","lines":["a"]},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"insert","lines":["s"]},{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"remove","lines":["s"],"id":839},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"remove","lines":["s"]},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"remove","lines":["a"]},{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":84,"column":12},"end":{"row":84,"column":13},"action":"insert","lines":["r"],"id":840},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"insert","lines":["e"]},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"insert","lines":["t"]},{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"insert","lines":["u"]},{"start":{"row":84,"column":16},"end":{"row":84,"column":17},"action":"insert","lines":["r"]},{"start":{"row":84,"column":17},"end":{"row":84,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":84,"column":18},"end":{"row":84,"column":19},"action":"insert","lines":[" "],"id":841},{"start":{"row":84,"column":19},"end":{"row":84,"column":20},"action":"insert","lines":["R"]},{"start":{"row":84,"column":20},"end":{"row":84,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":84,"column":19},"end":{"row":84,"column":21},"action":"remove","lines":["Re"],"id":842},{"start":{"row":84,"column":19},"end":{"row":84,"column":39},"action":"insert","lines":["ReactionDoesNotExist"]}],[{"start":{"row":83,"column":23},"end":{"row":83,"column":24},"action":"remove","lines":["."],"id":843}],[{"start":{"row":83,"column":23},"end":{"row":83,"column":24},"action":"insert","lines":["."],"id":844}],[{"start":{"row":84,"column":17},"end":{"row":84,"column":18},"action":"remove","lines":["n"],"id":845},{"start":{"row":84,"column":16},"end":{"row":84,"column":17},"action":"remove","lines":["r"]},{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"remove","lines":["u"]},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"remove","lines":["t"]},{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":84,"column":13},"end":{"row":84,"column":14},"action":"insert","lines":["a"],"id":846},{"start":{"row":84,"column":14},"end":{"row":84,"column":15},"action":"insert","lines":["i"]}],[{"start":{"row":84,"column":15},"end":{"row":84,"column":16},"action":"insert","lines":["s"],"id":847},{"start":{"row":84,"column":16},"end":{"row":84,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":117,"column":23},"end":{"row":117,"column":24},"action":"insert","lines":["."],"id":848}],[{"start":{"row":118,"column":17},"end":{"row":118,"column":18},"action":"remove","lines":["n"],"id":849},{"start":{"row":118,"column":16},"end":{"row":118,"column":17},"action":"remove","lines":["r"]},{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"remove","lines":["u"]},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"remove","lines":["t"]},{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"insert","lines":["a"],"id":850},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"insert","lines":["i"]},{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"insert","lines":["s"]},{"start":{"row":118,"column":16},"end":{"row":118,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"remove","lines":["t"],"id":851},{"start":{"row":95,"column":26},"end":{"row":95,"column":27},"action":"remove","lines":["e"]},{"start":{"row":95,"column":25},"end":{"row":95,"column":26},"action":"remove","lines":["g"]}],[{"start":{"row":95,"column":25},"end":{"row":95,"column":26},"action":"insert","lines":["f"],"id":852},{"start":{"row":95,"column":26},"end":{"row":95,"column":27},"action":"insert","lines":["i"]},{"start":{"row":95,"column":27},"end":{"row":95,"column":28},"action":"insert","lines":["l"]},{"start":{"row":95,"column":28},"end":{"row":95,"column":29},"action":"insert","lines":["t"]},{"start":{"row":95,"column":29},"end":{"row":95,"column":30},"action":"insert","lines":["e"]},{"start":{"row":95,"column":30},"end":{"row":95,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"remove","lines":["t"],"id":853},{"start":{"row":129,"column":26},"end":{"row":129,"column":27},"action":"remove","lines":["e"]},{"start":{"row":129,"column":25},"end":{"row":129,"column":26},"action":"remove","lines":["g"]}],[{"start":{"row":129,"column":25},"end":{"row":129,"column":26},"action":"insert","lines":["f"],"id":854},{"start":{"row":129,"column":26},"end":{"row":129,"column":27},"action":"insert","lines":["i"]},{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"insert","lines":["l"]},{"start":{"row":129,"column":28},"end":{"row":129,"column":29},"action":"insert","lines":["t"]},{"start":{"row":129,"column":29},"end":{"row":129,"column":30},"action":"insert","lines":["e"]},{"start":{"row":129,"column":30},"end":{"row":129,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":134,"column":39},"end":{"row":134,"column":40},"action":"remove","lines":["C"],"id":855}],[{"start":{"row":134,"column":39},"end":{"row":134,"column":40},"action":"insert","lines":["c"],"id":856}],[{"start":{"row":14,"column":4},"end":{"row":25,"column":31},"action":"remove","lines":["def create_post(self, user_id: int, post_content: str) -> int:","        post_obj = Post.objects.create(","            posted_by_id=user_id,","            content=post_content","        )","","        post_id = post_obj.id","        return post_id","","    def is_valid_post_id(self, post_id: int) -> bool:","        is_post_id_valid = Post.objects.filter(id=post_id).exists()","        return is_post_id_valid"],"id":857},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":53,"column":0},"action":"remove","lines":["","    def create_comment(self, user_id: int, post_id: int,","                       comment_content: str) -> int:","        comment_obj = Comment.objects.create(","            commented_by_id=user_id,","            post_id=post_id,","            content=comment_content","        )","","        comment_id = comment_obj.id","        return comment_id","","    def is_valid_comment_id(self, comment_id: int) -> bool:","        is_comment_id_valid = Comment.objects.filter(id=comment_id).exists()","        return is_comment_id_valid","","    def parent_id_exists_return_id(self, comment_id: int) -> int:","        comment_obj = Comment.objects.get(id=comment_id)","        parent_comment_id = comment_obj.parent_comment_id","        return parent_comment_id","","    def post_id_of_given_comment_id(self, comment_id: int) -> int:","        comment_obj = Comment.objects.get(id=comment_id)","        post_id = comment_obj.post_id","        return post_id","","    def reply_to_comment(self, user_id: int,","                         post_id: int,","                         comment_id: int,","                         reply_content: str) -> int:","        comment_obj = Comment.objects.create(","            commented_by_id=user_id,","            post_id=post_id,","            comment_id=comment_id,","            content=reply_content","        )","","        comment_id = comment_obj.id","        return comment_id",""],"id":858}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":859}],[{"start":{"row":99,"column":4},"end":{"row":137,"column":0},"action":"remove","lines":["def is_valid_user_to_delete_post(self, user_id: int,","                                     post_id: int) -> bool:","        is_authorized_user = Post.objects.filter(","            id=post_id,","            posted_by_id=user_id).exists()","        return is_authorized_user","","    def delete_post(self, user_id: int, post_id: int):","        Post.objects.get(","            id=post_id,","            posted_by_id=user_id).delete()","","    def get_posts_with_more_positive_reactions(self) -> List[int]:","","        from fb_post_v2.constants.constants import (","            POSITIVE_REACTIONS,","            NEGATIVE_REACTIONS","        )","","        positive_count = Count('reactions', filter=Q(","            reactions__reaction__in=POSITIVE_REACTIONS))","","        negative_count = Count('reactions', filter=Q(","            reactions__reaction__in=NEGATIVE_REACTIONS))","","        post_objs_ids = list(Post.objects.annotate(p_count=positive_count)\\","                             .annotate(n_count=negative_count)\\","                             .filter(p_count__gt=F('n_count'))\\","                             .values_list('id', flat=True))","","        return post_objs_ids","","    def get_posts_reacted_by_user(self, user_id: int) -> List[int]:","        user_reacted_post_ids = list(Post.objects.filter(","                reactions__reacted_by_id=user_id)\\","                .values_list('id', flat=True))","","        return user_reacted_post_ids",""],"id":860},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":98,"column":0},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":861}],[{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["t"],"id":862},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["s"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["o"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["P"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":[" "]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["t"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["r"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["o"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["p"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["m"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"remove","lines":["i"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"remove","lines":[" "]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["t"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["s"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["o"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["p"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["."]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["s"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["l"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["e"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["d"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["o"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["m"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["."]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["2"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["v"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["_"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["s"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["o"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["p"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["_"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["b"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["f"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":[" "],"id":863},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"remove","lines":["m"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"remove","lines":["o"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["r"]},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["f"]},{"start":{"row":5,"column":45},"end":{"row":6,"column":0},"action":"remove","lines":["",""]},{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"remove","lines":["t"]},{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"remove","lines":["n"]},{"start":{"row":5,"column":42},"end":{"row":5,"column":43},"action":"remove","lines":["e"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"remove","lines":["m"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"remove","lines":["m"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"remove","lines":["o"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"remove","lines":["C"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":[" "]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["t"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["r"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"remove","lines":["o"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"remove","lines":["p"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":["m"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"remove","lines":["i"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":[" "]}],[{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["t"],"id":864},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["n"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["e"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["m"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["m"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["o"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":["c"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":["."]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["s"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["l"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["e"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["d"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"remove","lines":["o"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["m"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["."]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["2"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["v"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"remove","lines":["_"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":["t"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":["s"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["o"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["p"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["_"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["b"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"remove","lines":["f"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"remove","lines":[" "]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"remove","lines":["m"]}],[{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"remove","lines":["o"],"id":865},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"remove","lines":["r"]},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["f"]}],[{"start":{"row":4,"column":48},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":866}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":["r"],"id":867},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["e"]},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["a"]},{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":["c"]},{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"insert","lines":["t"]},{"start":{"row":2,"column":42},"end":{"row":2,"column":43},"action":"insert","lines":["i"]},{"start":{"row":2,"column":43},"end":{"row":2,"column":44},"action":"insert","lines":["o"]},{"start":{"row":2,"column":44},"end":{"row":2,"column":45},"action":"insert","lines":["n"]},{"start":{"row":2,"column":45},"end":{"row":2,"column":46},"action":"insert","lines":["_"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["R"],"id":868},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["e"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["a"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["c"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["t"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["i"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["R"],"id":869},{"start":{"row":10,"column":29},"end":{"row":10,"column":30},"action":"insert","lines":["e"]},{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["a"]},{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["c"]},{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["t"]},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["i"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["o"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["R"],"id":870},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["e"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["a"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["c"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["t"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["i"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["n"],"id":871}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":9},"end":{"row":18,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590125771615,"hash":"a0020d527c4b0bd037371e8dde5f0342432bb61e"}