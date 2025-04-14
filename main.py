from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.event.filter import command, regex, llm_tool, permission_type, PermissionType
import numpy as np

@register("LLM四则运算工具", "灵煞", "让你的AI精确回答简单数学题", "1.0.0")
class FFRtools(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @llm_tool(name="FFRadd")
    async def FFRadd(self, event: AstrMessageEvent, num1: float, num2: float) -> MessageEventResult:
        '''当用户询问两个数的和时

    Args:
        num1(number): 第一个数字
        num2(number): 第二个数字
    '''
        answer0 = np.add(num1 ,num2)
        answer = np.around(answer0, 3)
        result = f"按照你的人设回答用户结果是:{answer}。" 
        return result
        
    @llm_tool(name="FFRminus")
    async def FFRminus(self, event: AstrMessageEvent, num1: float, num2: float) -> MessageEventResult:
        '''当用户询问两个数的差时

    Args:
        num1(number): 第一个数字
        num2(number): 第二个数字
    '''
        answer0 = np.subtract(num1 ,num2)
        answer = np.around(answer0, 3)
        result = f"按照你的人设回答用户结果是:{answer}。" 
        return result

    @llm_tool(name="FFRdid")
    async def FFRdid(self, event: AstrMessageEvent, num1: float, num2: float) -> MessageEventResult:
        '''当用户询问两个数的商时

    Args:
        num1(number): 第一个数字
        num2(number): 第二个数字
    '''
        answer0 = np.divide(num1 ,num2)
        answer = np.around(answer0, 3)
        result = f"按照你的人设回答用户结果是:{answer}。" 
        return result
            
    @llm_tool(name="FFRmul")
    async def FFRmul(self, event: AstrMessageEvent, num1: float, num2: float) -> MessageEventResult:
        '''当用户询问两个数的乘积时

    Args:
        num1(number): 第一个数字
        num2(number): 第二个数字
    '''
        answer0 = np.multiply(num1 ,num2)
        answer = np.around(answer0, 3)
        result = f"按照你的人设回答用户结果是:{answer}。" 
        return result
        
    @llm_tool(name="FFRcomp")
    async def FFRcomp(self, event: AstrMessageEvent, num1: float, num2: float) -> MessageEventResult:
        '''当用户询问两个数的大小时

    Args:
        num1(number): 第一个数字
        num2(number): 第二个数字
    '''
        answer = np.subtract(num1 ,num2)
        if answer > 0:
           result = "按照你的人设回答用户结果是:第一个数字大于第二个数字。" 
           return result   
        if answer < 0:
           result = "按照你的人设回答用户结果是:第一个数字小于第二个数字。" 
           return result   
        else:
           result = "按照你的人设回答用户结果是:这是同一个数字。" 
           return result   