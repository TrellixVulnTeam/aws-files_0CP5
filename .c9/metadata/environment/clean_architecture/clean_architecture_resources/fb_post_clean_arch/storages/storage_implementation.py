{"filter":false,"title":"storage_implementation.py","tooltip":"/clean_architecture/clean_architecture_resources/fb_post_clean_arch/storages/storage_implementation.py","ace":{"folds":[],"scrolltop":4006,"scrollleft":0,"selection":{"start":{"row":270,"column":52},"end":{"row":270,"column":52},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":239,"state":"start","mode":"ace/mode/python"}},"hash":"37941ca6a24fce89bd435aad8cf6dc6a0d7af1a2","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":168,"column":4},"end":{"row":175,"column":23},"action":"remove","lines":["@staticmethod","    def _convert_post_obj_to_dto(post):","        post_dto = PostDto(user_id=post.user.id,","                           post_content=post.post_content,","                           pub_date_time=post.pub_date_time.replace(","                               tzinfo=None),","                           post_id=post.id)","        return post_dto"],"id":2}],[{"start":{"row":168,"column":0},"end":{"row":168,"column":4},"action":"remove","lines":["    "],"id":3},{"start":{"row":167,"column":0},"end":{"row":168,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":320,"column":24},"end":{"row":321,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":321,"column":0},"end":{"row":321,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":321,"column":4},"end":{"row":321,"column":8},"action":"remove","lines":["    "],"id":5},{"start":{"row":321,"column":0},"end":{"row":321,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":321,"column":0},"end":{"row":322,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":322,"column":0},"end":{"row":322,"column":4},"action":"insert","lines":["    "],"id":7}],[{"start":{"row":322,"column":4},"end":{"row":329,"column":23},"action":"insert","lines":["@staticmethod","    def _convert_post_obj_to_dto(post):","        post_dto = PostDto(user_id=post.user.id,","                           post_content=post.post_content,","                           pub_date_time=post.pub_date_time.replace(","                               tzinfo=None),","                           post_id=post.id)","        return post_dto"],"id":8}]]},"timestamp":1590159781723}