from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("auto_image_text", "your_name", "当只有图片时自动加一段文本", "0.1.0")
class AutoImageText(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.on_message()
    async def handle_message(self, event: AstrMessageEvent):
        # 没有文字，但有图片
        if event.is_image() and not event.has_text():
            # 自动附加一句话
            extra = "（自动附加：请描述图片内容）"
            event.append_text(extra)

            # 返回一条提示消息（可选）
            yield event.plain_result(f"已附加文本: {extra}")

    @filter.on_astrbot_loaded()
    async def on_loaded(self):
        print("AutoImageText 插件已加载！持续监听消息。")
