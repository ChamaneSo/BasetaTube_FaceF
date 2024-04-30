from typing import Optional
import gradio

from facefusion import metadata, wording

ABOUT_BUTTON : Optional[gradio.HTML] = None
DONATE_BUTTON : Optional[gradio.HTML] = None


def render() -> None:
	global ABOUT_BUTTON
	global DONATE_BUTTON

	ABOUT_BUTTON = gradio.HTML(
		value='<img src="file/logo.png" />'
	)
	DONATE_BUTTON = gradio.Button(
		value = 'Code Modifie par @Mafluenceur-Team',
		link = 'https://mafluenceur.com/',
		size = 'sm'
	)
