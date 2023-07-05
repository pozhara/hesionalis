from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.views.generic import ListView

from core.models import Artist, Design

# Create your views here.

faqs = [
    {
        "question": "How do I book an appointment?",
        "answer": "Provide information about the booking process, such as whether appointments are made online, over the phone, or in person. Mention any specific requirements or steps involved in securing a tattoo appointment."
    },
    {
        "question": "Is there a minimum age requirement for getting a tattoo?",
        "answer": "Explain the legal age requirements for getting a tattoo in your location. If there are any additional policies or restrictions regarding age, such as parental consent for minors, include that information as well."
    },
    {
        "question": "How much does a tattoo cost?",
        "answer": "Address the question of pricing by explaining that tattoo costs vary depending on factors such as the size, design complexity, placement, and the artist's experience. Consider providing a general price range or mentioning that pricing is determined during a consultation."
    },
    {
        "question": "Do you require a deposit for appointments?",
        "answer": "Inform customers about your deposit policy, including whether a deposit is required to secure an appointment and any refund or rescheduling policies associated with deposits."
    },
    {
        "question": "How should I prepare for my tattoo appointment?",
        "answer": "Offer guidance on how clients should prepare themselves before their appointment, such as avoiding alcohol or blood-thinning medications, staying hydrated, and eating a good meal beforehand."
    },
    {
        "question": "What safety measures do you have in place?",
        "answer": "Highlight the importance of safety and cleanliness in your studio. Explain the measures you take to ensure a sterile environment, including the use of disposable needles, sterilization techniques, and adherence to health regulations."
    },
    {
        "question": "Can I bring my own design, or do you provide custom designs?",
        "answer": "Explain whether clients can bring their own tattoo design ideas or if you offer custom design services. Describe any consultation process involved in turning their ideas into a unique tattoo design."
    },
    {
        "question": "How long does the tattoo process take?",
        "answer": "Provide a general estimate of the time required for different tattoo sizes or design complexities. Emphasize that tattooing is a meticulous process and that the duration can vary depending on factors like the design, client comfort, and breaks."
    },
    {
        "question": "How do I take care of my tattoo after getting it done?",
        "answer": "Offer aftercare instructions to help clients properly care for their new tattoo. Include information on cleaning, moisturizing, avoiding direct sunlight, and any specific aftercare products you recommend."
    },
    {
        "question": "Can I see examples of your previous work?",
        "answer": "Direct clients to your portfolio, either on your website or social media platforms, where they can view examples of your artists' previous work. Highlight the versatility and quality of your artists' tattooing styles."
    }
]


reviews = [
    {
        "user": "David Radyson",
        "review": "Wonderful friendly staff! Super clean studio, welcoming atmosphere! Thank you so much for my awesome tattoos! Also given free beverages while I was going through ideas."
    },
    {
        "user": "Marcus Andreson",
        "review": "What a great place to go! I've been to a lot of places but I have never been anywhere that compares to this upbeat and modern studio. Thank you for the tattoo!"
    },
    {
        "user": "Matt Smith",
        "review": "I used various studios in the city and they didn't make the cut... so I went to try Neolagnium. These guys know exactly what they are doing. Top quality studio! Top atmosphere!"
    },
    {
        "user": "Sarah Thompson",
        "review": "I had an amazing experience at Neolagnium! The artists were extremely talented and took the time to understand what I wanted. The studio has a great vibe and I felt comfortable throughout the entire process. Highly recommend!"
    },
    {
        "user": "Emily Johnson",
        "review": "Neolagnium is the best tattoo studio in town! The artists are not only skilled but also very friendly and accommodating. The studio itself is clean and well-maintained. I couldn't be happier with the tattoo I got from them. Definitely my go-to place from now on!"
    }
]


class HomeView(View):
    def get(self, request):
        artists = Artist.objects.all()
        return render(request, 'index.html', context={"artists": artists, "reviews": reviews})


class FAQView(View):

    def get(self, request):

        return render(request, 'faq.html', context={'faqs': faqs})


class ArtistView(ListView):
    model = Artist
    template_name = 'artists.html'
    context_object_name = 'artists'
    
    
class DesignsView(View):
    def get(self, request):
        designs = Design.objects.all()
        size = ['large', "medium", "small"]
        return render(request, 'styles.html', context={'size': size, "designs": designs})
