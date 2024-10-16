def create_bow_vector(sentence):
  # Tokenize the sentence into words
  words = sentence.split()

  # Create a vocabulary dictionary
  vocabulary = {}
  for word in words:
    if word not in vocabulary:
      vocabulary[word] = len(vocabulary)

  # Create a BoW vector
  bow_vector = [0] * len(vocabulary)

  # Count the occurrences of each word
  for word in words:
    index = vocabulary[word]
    bow_vector[index] += 1

  return bow_vector

# Example usage:
sentence = "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and human language."
bow_vector = create_bow_vector(sentence)
print(bow_vector)