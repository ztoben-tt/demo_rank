from django.shortcuts import render
from django.http import HttpResponse

from .models import ScoreModel


# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse('ok')


def upload(request):
    """
    上传客户端号和分数
    :param request:
    :return:
    """
    # 接收参数
    user_id = request.post.get('user_id')
    score = request.post.get('score')
    if not user_id:
        return HttpResponse('请传入客户端号')
    if not score or score < 1 or score > 10000000:
        return HttpResponse('请输入正确的分数')
    # 查询记录
    user_db_info = ScoreModel.objects.filter(user_id=user_id).first()
    # 无记录,创建
    if not user_db_info:
        ScoreModel.objects.create(user_id=user_id, score=score)
    # 有记录,更新
    else:
        user_db_info.score = score
        user_db_info.save()
    return HttpResponse('上传成功')


def rank(request):
    """
    排名
    :param request:
    :return:
    """
    user_id = request.POST.get('user_id')
    start = request.POST.get('start')
    end = request.POST.get('end')
    if not user_id:
        return HttpResponse('请传入客户端号')
    user_db_info = ScoreModel.objects.all().order_by('-score')
    num, result_list, user_now_dict = 1, [], {}
    # 排名
    for user_info in user_db_info:
        user_dict = dict()
        user_dict['rank'] = num
        user_dict['user_id'] = user_info.user_id
        user_dict['score'] = user_info.score
        if user_id == user_info.user_id:
            user_now_dict = user_dict.copy()
        result_list.append(user_dict)
        num += 1
    # end for user_info in user_db_info:
    if not start and not end:
        result_list.append(user_now_dict)
    else:
        result_list = result_list[start-1:end]
        result_list.append(user_now_dict)
    return result_list

# 测试

