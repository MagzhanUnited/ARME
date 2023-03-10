from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Person, Product, Message
from .serializers import PersonSerializer, ProductSerializer, MessageSerializer
import openai

openai.api_key = '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'

@api_view(['GET'])
def getPersons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getPerson(request, email, password):
    person = Person.objects.get(password = password, email = email)
    serializer = PersonSerializer(person, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def getPersonID(request, id):
    person = Person.objects.get(id = id)
    serializer = PersonSerializer(person, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def getPersonalPruduct(request, id):
    products = Product.objects.filter(seller = id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPerson(request):
    data = request.data
    person = Person.objects.create(
        email = data['email'],
        password = data['password'],
        number = data['number'],
        fullname = data['fullname'],
    )
    serializer = PersonSerializer(person, many = False)
    person.save()
    return Response(serializer.data)

@api_view(['POST'])
def postMessage(request):
    data = request.data
    person = Person.objects.get(id = data['user'])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=data['question'],
        temperature=0.3,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    message = Message.objects.create(
        user = person,
        question = data['question']
    )
    message.answer = response['choices'][0]['text']
    serializer = MessageSerializer(message, many = False)
    message.save()
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    person = Person.objects.get(id=data['seller'])
    product = Product.objects.create(
        title = data['title'],
        text = data['text'],
        price = data['price'],
        image = data['image'],
        states = data['states'],
        isDeliver = data['isDeliver'],
        city = data['city'],
        seller = person,
        cartype = data['cartype'],
        #views = data['views'],
        #likes = data['likes']
    )
    serializer = ProductSerializer(product, many = False)
    product.save()
    return Response(serializer.data)

@api_view(['PUT'])
def liking(request, pk):
    product = Product.objects.get(id = pk)
    person_id = request.data.get('id')
    try:
        #person = Person.objects.get(id=request['id'])
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return Response({'error': 'Person does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if person not in product.likes.all():
        person.liked.add(product)
        product.likes.add(person)
        product.save()
        return Response({'success': 'Person added to views and likes'}, status=status.HTTP_200_OK)
    else:
        product.likes.remove(person)
        person.liked.remove(product)
        return Response({'error': 'Person already exists in views or likes'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def views(request, pk):
    product = Product.objects.get(id = pk)
    person_id = request.data.get('id')
    try:
        person = Person.objects.get(id = person_id)
        
    except Person.DoesNotExist:
        return Response({'error': 'Person does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if person not in product.views.all():
        product.views.add(person)
        product.save()
        return Response({'success': 'Person added to views and likes'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Person already exists in views or likes'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id = pk)
    product.delete()

    return Response('successfuly deleted')

@api_view(['GET'])
def getProduct(request, id):
    person = Person.objects.get(id = id)
    products = Product.objects.filter(id__in = person.liked.all())
    #result = [product for product in products if product['id'] in person.liked]
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request, id):
    message = Message.objects.filter(user = id)
    serializer = MessageSerializer(message, many = True)
    return Response(serializer.data)


    

