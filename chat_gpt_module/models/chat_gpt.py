# models/chat_gpt.py

from transformers import pipeline # type: ignore
from odoo import models, fields, api # type: ignore


class ChatGPT(models.Model):
    name = 'chat_gpt'
    description = 'Chat GPT Model'

    name = fields.Char(string="User_Input", required=True)
    response = fields.Text(string="Response")

    @api.model
    def generate_response(self, input_text):
        chatbot = pipeline("text-generation", model="gpt2")
        response = chatbot(input_text)
        return response[0]['generated_text']
    
        openai_endpoint = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': 'openiatoken',
            'Content-Type': 'application/transformers'
        }
    def get_output(self):
        for record in self:
            if record.user_input:
                output_text = self.send_request_to_openai(record.user_input)
                                
                if output_text is not None:
                    record.output = output_text
                else:
                    record.output = "please configure the connection"
    